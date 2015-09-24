#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

import socket, os

fname = "all_numbers.txt"
os.system("rm -rf data/split")
os.system("mkdir -p data/split")
# TOTAL
osp = os.popen("wc -l data/" + fname)
TOTAL = 0
for line in osp:
    TOTAL = int(line.split()[0])
    break
osp.close()
SPLIT = 6

block = TOTAL / SPLIT + 1
host = socket.gethostname()
host = "dev6"
index = int(list(host)[-1])
start = block * (index - 1)
end = start + block
if end > TOTAL:
    end = TOTAL

diff = end - start
CMD = "head -%d data/%s | tail -%d  > data/split.txt" % (end, fname, diff)

print(CMD)
os.system(CMD)

## Split file
CMD = "cp data/split.txt data/split ; cd data/split ; split -l 1000 split.txt; rm split.txt"
os.system(CMD)
