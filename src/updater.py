#!/usr/bin/env python3

import requests

def check_update(version):

    URL = "https://raw.githubusercontent.com/DocBox12/RODO-CV/version/master.txt"
    url_more_information = "https://github.com/DocBox12/RODO-CV/releases"
    website_data = requests.get(URL)
    if website_data.status_code == 200:
        # remove all white chars
        raw_data_from_website = website_data.content.decode("utf-8").rstrip('\r\n\t')
    else:
        return
    
    if str(version) == str(raw_data_from_website):
        return
    else:
        warning = "Pojawiła się nowa wersja RODO-CV oznaczona numerem %s. Ty posiadasz wersję %s. Wejdź na stronę %s i dokonaj aktualizacji." % (raw_data_from_website, version, url_more_information)
        return warning

    return


