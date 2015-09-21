#!/usr/bin/env bash

echo "CLone from git"
git clone https://github.com/Lhfcws/SregCrawler

echo "Build virtualenv"
cd SregCrawler
virtualenv env
source env/bin/activate

echo "pip installing"
pip install urlparse2 chardet
pip install requests==2.5.3

echo "Begin split"
cd youzan
python split.py

echo "deploy done"

echo "Please run command: "
echo "source env/bin/activate && nohup python youzan.py &"