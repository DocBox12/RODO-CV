#!/usr/bin/env python3

import os
import argparse

VERSION = "1.1-alpha"

def install():

    execute_command = ("""
                        git init
                        git pull https://gitlab.com/DocBox12/rodo-cv.git
                        virtualenv -p python3 .
                        ./bin/pip3 install fpdf
                        ./bin/pip3 install PyPDF3
                        ./bin/pip3 install requests
                        chmod +x ./src/rodocv.py
                        """)

    os.system(execute_command)

    return


def update():
    os.system("git pull https://gitlab.com/DocBox12/rodo-cv.git")
    exit()


def force_update():
    execute_command = ("""
                        git reset --hard
                        git pull https://gitlab.com/DocBox12/rodo-cv.git
                        chmod +x ./src/rodocv.py
                        """)

    os.system(execute_command)
    exit()

def reset_app():
    os.system("git reset --hard")
    return

def check_update():
    try:
        import src.updater
    except:
        print("Najpierw zainstaluj aplikację.")
        return
    value = src.updater.search_update(VERSION)
    if value is True:
        print("Czy chcesz dokonać aktualizacji? [T = TAK] [N = NIE]")
        while True:
            choose = input()
            if choose.upper() == "T":
                check_type_update()
            elif choose.upper() == "N":
                print("Aktualizacja została przerwana na żądanie użytkownika")
                exit()
            else:
                print("Zły wybór, spróbuj ponownie.")
    else:
        print("Posiadasz najnowszą wersję")


    return


def check_type_update():
    import requests
    URL = "https://github.com/DocBox12/RODO-CV/blob/version/warning.txt"
    more_information = "https://github.com/DocBox12/RODO-CV/releases"
    website_data = requests.get(URL)
    if website_data.status_code == 200:
        # Remove all white chars
        raw_data_from_website = website_data.content.decode("utf-8").rstrip('\r\n\t')
    else:
        print("Nie mogę pobrać danych. Aktualizacja została przerwana.")
        exit()
    
    if str(raw_data_from_website).upper() == "YES":
        print("UWAGA! Wykryto, że najnowsza aktualizacja zmienia ważne pliki, które są niezbędne do działania aktualizacji. Przeczytaj informacje o wydaniu aby dowiedzieć się więcej. %s") % (more_information)
        print("Czy chcesz kontynuować? [T=TAK] [N=NIE]")
        while True:
            choose = input()
            if choose.upper() == "T":
                force_update()
            elif choose.upper() == "N":
                print("Aktualizacja została przerwana na żądanie użytkownika.")
                exit()
            else:
                print("Zły wybór, spróbuj ponownie.")
    else:
        update()
    

def question():
    print("\n Czy chcesz dokonać aktualizacji [T=TAK] [N=NIE]")
    return



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--install", help="Instaluje wirtualne środowisko Pythona 3 i pobiera najnowszą wersję aplikacji z serwera", action="store_true")

    parser.add_argument("--check_update", help="Instaluje wirtualne środowisko Pythona 3 i pobiera najnowszą wersję aplikacji z serwera", action="store_true")

    parser.add_argument("--force_update", help="Przywraca stan aplikacji do oficjalnego wydania i pobiera najnowszą wersję z serwera. Wszystkie twoje ustawienia zostaną usunięte", action="store_true")

    parser.add_argument("--reset", help="Przywraca aplikację do pierwotnego stanu. Wszystkie twoje ustawienia zostaną usunięte", action="store_true")

    args = parser.parse_args()


    if args.install:
        install()
    
    if args.force_update:
        force_update()
    
    if args.reset:
        reset_app()

    if args.check_update:
        check_update()
