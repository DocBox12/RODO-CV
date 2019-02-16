#!/bin/bash

# Maintainer DocBox12
# Website: https://docbox12.github.io/

set -e

git init
git pull https://gitlab.com/DocBox12/rodo-cv.git
virtualenv -p python3 .
./bin/pip3 install fpdf
./bin/pip3 install PyPDF3
./bin/pip3 install requests
chmod +x install.py
chmod +x ./src/rodocv.py
rm install.sh