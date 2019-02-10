#!/usr/bin/env python3

import requests
import os

def check_update(version):

    URL = ""
    url_more_information = "https://github.com/DocBox12/RODO-CV/releases"
    website_data = requests.get(URL)
    if website_data.status_code == 200:
        # Remove all white chars
        raw_data_from_website = website_data.content.decode("utf-8").rstrip('\r\n\t')
    else:
        return
    
    if str(version) == str(raw_data_from_website):
        return
    else:
        info = "Pojawiła się nowa wersja RODO-CV oznaczona numerem %s. Ty posiadasz wersję %s. Możesz dokonać aktualizacji, jednak przed jej dokonaniem zapoznaj się z informacjami odnośnie wydania na strone internetowej %s." % (raw_data_from_website, version, url_more_information)
        print(info)
        
    return