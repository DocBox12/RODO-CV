#!/usr/bin/env python3

import os
import requests
import src.updater

VERSION = "1.1-alpha"

def install():

    execute_command = ("""
                        git init
                        git pull https://gitlab.com/DocBox12/rodo-cv.git
                        virtualenv -p python3 .
                        ./bin/pip3 install fpdf
                        ./bin/pip3 install PyPDF3
                        ./bin/pip3 install requests
                        """)

    os.system(execute_command)

    return


def update():
    os.system("git pull https://gitlab.com/DocBox12/rodo-cv.git")
    return


def force_update():
    execute_command = ("""
                        git reset --hard HEAD
                        git https://gitlab.com/DocBox12/rodo-cv.git
                        """)

def check_type_update():
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

def question():
    print("\n Czy chcesz dokonać aktualizacji [T=TAK] [N=NIE]")
    return


