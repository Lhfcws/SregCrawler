#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

import glob, json

url_field = ["cellphone_url", "email_url", "user_url"]
websites = {}
plugins = glob.glob("./plugins/*.json")
for pluginf in plugins:
    with open(pluginf, "r", encoding="utf-8") as f:
        try:
            plugin = json.load(f)
            site = plugin["information"]["website"]
            req = plugin["request"]
            websites.setdefault(site, [None, None, None])
            for i, u in enumerate(url_field):
                if req[u] != "":
                    websites[site][i] = req[u]
        except Exception as e:
            print(str(e) + str(pluginf))
            continue


stat = [0, 0, 0]
for k, v in websites.items():
    for i, u in enumerate(v):
        if u is not None:
            stat[i] += 1

print("Total plugins: %d, Total websites: %d" % (len(plugins), len(websites)))
print("Cellphone: %d, Email: %d, User: %d" % (stat[0], stat[1], stat[2]))
