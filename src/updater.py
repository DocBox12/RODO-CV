#!/usr/bin/env python3

import requests
import os


def news():
    URL_NEWS = ""
    website_data = requests.get(URL_NEWS)
    if website_data.status_code == 200:
        # Remove all white chars
        raw_data_from_website = website_data.content.decode("utf-8").rstrip('\r\n\t')
        return raw_data_from_website
    else:
        return


def check_version(version):
    URL_PREVIOUS_VERSION = ""
    website_data = requests.get(URL_PREVIOUS_VERSION)
    if website_data.status_code == 200:
        # Remove all white chars
        previous_version = website_data.content.decode("utf-8").rstrip('\r\n\t')
    else:
        print("Nie mogę pobrać danych odnośnie aktualizacji. Koniec procesu.")
        print(website_data.status_code)
        exit()
        if str(version) == str(previous_version):
            warning()
        else:
            print("Posiadasz za starę wersję aby dokonać automatycznej aktualizacji. Musisz wykonać ręcznie aktualizację do nowej wersji. ")


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
        warning = "Pojawiła się nowa wersja RODO-CV oznaczona numerem %s. Ty posiadasz wersję %s. Wejdź na stronę %s i dokonaj aktualizacji." % (raw_data_from_website, version, url_more_information)
        return warning

    return

def warning():
    URL_WARNING = ""
    website_data = requests.get(URL_WARNING)
    if website_data.status_code == 200:
        # Remove all white chars
        raw_data_from_website = website_data.content.decode("utf-8").rstrip('\r\n\t')
        print(raw_data_from_website)
        print("Czy chcesz kontynuować? y - tak // n - nie \n")
        while True:
            choose = input("")
            if choose.lower() == "y":
                upgrade()
                break
            elif choose.lower() == 'n':
                print("Aktualizacja nie została wykonana na żądanie użytkownika.")
                break
            else:
                print("Zły wybór, spróbuj jeszcze raz... \n")
                continue

    else:
        print("Nie mogą pobrać listy plików. Proces został przerwany.")
        print(website_data.status_code)
        exit()
    return

def upgrade():
    URL = ""
    website_data = requests.get(URL)
    if website_data.status_code == 200:
        # Remove all white chars
        raw_data_from_website = website_data.content.decode("utf-8").rstrip('\r\n\t')
    else:
        print("Nie mogą pobrać listy plików. Proces został przerwany.")
        print(website_data.status_code)
        exit()

    LIST_links_and_filenames = raw_data_from_website.split("\n")
    
    for i in range(len(LIST_links_and_filenames)):
        elements = LIST_links_and_filenames[i].split(";")
        link = elements[0]
        file_name = elements[1]
        get_source_from_website = requests.get(link)
        if get_source_from_website.status_code == 200:
            raw_source_file = get_source_from_website.content.decode("utf-8")
        else:
            print("Nie pobrac pobrać listy plików do aktualizacji. Proces został przerwany")
            print(get_source_from_website.status_code)
            exit()

        path = os.path.join(os.path.dirname(__file__)) + "/" + file_name

        if os.path.exists is None:
            os.mknod(path)
        with open(path, 'w') as p:
            p.write(raw_source_file)
            p.close()
    
    return