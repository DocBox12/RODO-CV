#!/bin/bash

set -e

git init
git pull https://github.com/DocBox12/RODO-CV.git
virtualenv -p python3 .
./bin/pip3 install fpdf
./bin/pip3 install PyPDF3
./bin/pip3 install requests
chmod +x install.py
chmod +x ./src/rodocv.py
