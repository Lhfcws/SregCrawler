#!/usr/bin/python
# coding: utf-8
__author__ = 'lhfcws'

import socket, os

os.system("rm -f data/split")
os.system("mkdir -p data/split")
# TOTAL
TOTAL = 50000
SPLIT = 6

block = TOTAL / SPLIT + 1
host = socket.gethostname()
# host = "dev6"
index = int(list(host)[-1])
start = block * (index - 1)
end = start + block
if end > TOTAL:
    end = TOTAL

diff = end - start
CMD = "head -%d data/all_numbers.txt | tail -%d  > data/split.txt" % (end, diff)

print(CMD)
os.system(CMD)

## Split file
CMD = "cp data/split.txt data/split ; cd data/split ; split split.txt -l 100 ; rm split.txt"
os.system(CMD)
