#!/usr/bin/env python
# encoding: utf-8
import sys, os, re, json, copy, glob
from multiprocessing import Pool

BUSINESS = ""
re_phone = re.compile("[0-9]+")

JSON_TMPL = {
    "id": "",
    "idType": "phone",
    "time": "2015-09-24 14:00:11",
    "ids": {
        # "1563278859": "qq",
        # "13825489654": "phone"
    },
    "properties": {
        # "birthday": "1992-08",
        # "sex": "男",
        # "province": "广东",
        # "city": "广州"
    },
    "footprint": {
        "content": "",
        "url": "",
        "fond": "",
        "count": 1,
        # "action": "购买",
        # "loc": "北京",
        "type": "",
        # "recipient": {"13874963215":"phone"}
    },
    "tags": [

    ]
}


def is_phone(p):
    if len(p) == 11 and re_phone.match(p) is not None:
        return True
    else:
        return False


def is_email(e):
    if e.count("@") > 0:
        return True
    else:
        return False


def build_plugins_dict():
    plugins = glob.glob("./plugins/*.json")
    d = {}

    for plugin in plugins:
        d[plugin["information"]["name"]] = (
        plugin["information"]["name"], plugin["information"]["category"], plugin["information"]["website"],
        plugin["information"]["desc"])

    return d


def parse_line(line):
    line = line.replace("[", "").replace("]", "").replace("(", "").replace(")", "")
    try:
        category, name, url = line.split()
    except Exception:
        return None
    return name, url


def main():
    result_root = BUSINESS + "/result/"
    jobs = []

    for xdir in os.listdir(result_root):
        jobs.append(result_root + xdir)

    pool = Pool(processes=5)
    pool.apply_async(func=work, args=jobs)
    pool.close()
    pool.join()
    print("Finish translating to json.")

def work(path):
    plugins = build_plugins_dict()
    for fl in os.listdir(path):
        user = copy.deepcopy(JSON_TMPL)
        user["id"] = sid = fl.split(".")[0]
        if is_phone(sid):
            user["idType"] = "phone"
        elif is_email(sid):
            user["idType"] = "email"

        os.system("mkdir -p %s/json" % BUSINESS)
        fw = open(BUSINESS + "/json/" + path.split("/")[-1] + ".json", "w", encoding="utf-8")
        with open(path + fl, "r", encoding="utf-8") as fp:
            for line in fp.readlines():
                line = line.strip()
                if line.startswith("[-"):
                    continue

                if line.startswith("["):
                    res = parse_line(line)
                    if res is None: continue
                    name, user["footprint"]["url"] = res
                    if name in plugins:
                        user["footprint"]["content"] = plugins[name][3]
                    fw.write(json.dumps(user, ensure_ascii=False))
                    fw.write("\n")
            fw.close()



####################
if __name__ == "__main__":
    BUSINESS = sys.argv[1]
    main()
