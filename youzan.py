import sys, os, time

def get_all_phones(fl):
    # return ["15800010588"]
    with open(fl, "r") as fp:
    # with open("youzan/data/all_numbers.txt", "r") as fp:
        ret = []
        for line in fp.readlines():
            ret.append(line.strip())
        return ret

def run(phones, dr):
    progress = 0
    path = "youzan/result/" + dr
    os.system("mkdir -p " + path)

    cmd = "python sreg.py -c %s > " + path + "/%s.txt"
    for phone in phones:
        os.system(cmd % (phone, phone))
        progress += 1
        print(phone + " done. " + str(progress))

def main():
    root = "youzan/data/split/"
    os.system("mkdir -p youzan/result")
    files = os.listdir(root)
    progress = 0

    res_files = os.listdir("youzan/result")

    for fl in files:
        if res_files.count(fl) > 0:
            print("[MAIN] Partition %s has been done, skip it." % fl)
            continue
        path = root + fl
        phones = get_all_phones(path)
        print("[MAIN] Get phones size: " + str(len(phones)) )
        run(phones, fl)
        progress += 100
        print("[MAIN] Run " + fl + " done. Progress: " + str(progress))

        os.system("rm reports/cellphone_*.html")

        # Sleep 2 seconds
        time.sleep(2)


if __name__ == "__main__":
    main()