#!/usr/bin/env python3

import requests
import os

def search_update(version):

    URL = "https://raw.githubusercontent.com/DocBox12/RODO-CV/version/stable.txt"
    website_data = requests.get(URL)
    if website_data.status_code == 200:
        # Remove all white chars
        raw_data_from_website = website_data.content.decode("utf-8").rstrip('\r\n\t')
    else:
        return
    
    if str(version) == str(raw_data_from_website):
        return False
    else:
        info = "INFO!!! \nPojawiła się nowa wersja RODO-CV oznaczona numerem %s. Ty posiadasz wersję %s. Możesz dokonać aktualizacji. Uruchom plik install.py" % (raw_data_from_website, version)
        print(info)
        
    return True


def news():
    return