#!/usr/bin/env python3

import os

def get_font(font_name):

    DICT_fonts = dict(
        arial = "arial.ttf",
        arial_bold = "arialbd.ttf",
        arial_italics_bold = "arialbi.ttf",
        arial_italics = "ariali.ttf",
        tahoma = "tahoma.ttf",
        times = "times.ttf",
        times_bold = "timesbd.ttf",
        times_italics_bold = "timesbi.ttf",
        times_italics = "timesi.ttf",
        verdana = "verdana.ttf",
        verdana_bold = "verdanab.ttf",
        verdana_italics = "verdanai.ttf",
        verdana_italics_bold = "verdanaz.ttf"
    )

    font_ttf = DICT_fonts.get(font_name)
    if font_ttf is None:
        print("Wpisana czcionka nie istnieje. Popraw błąd i uruchom program ponownie.")
        exit()
    font_path = os.path.join(os.path.dirname(__file__), font_ttf)
    if not os.path.exists(font_path):
        download_font(font_name)
        if os.path.exists(font_path):
            font_ttf = DICT_fonts.get(font_name)
            return font_ttf
        else:
            print("Nie mogę pobrać czcionki. Spróbuj uruchomić program jeszcze raz. Jeśli dalej będziesz widział ten komunikat to zgłoś problem na stronie projektu.")
            exit()
    else:
        return font_ttf

def download_font(font_name):
    DICT_fonts = dict(
        arial = "https://github.com/DocBox12/msfonts/raw/master/arial.ttf",
        arial_bold = "https://github.com/DocBox12/msfonts/raw/master/arialbd.ttf",
        arial_italics_bold = "https://github.com/DocBox12/msfonts/raw/master/arialbi.ttf",
        arial_italics = "https://github.com/DocBox12/msfonts/raw/master/ariali.ttf",
        tahoma = "https://github.com/DocBox12/msfonts/raw/master/tahoma.ttf",
        times = "https://github.com/DocBox12/msfonts/raw/master/times.ttf",
        times_bold = "https://github.com/DocBox12/msfonts/raw/master/timesbd.ttf",
        times_italics_bold = "https://github.com/DocBox12/msfonts/raw/master/timesbi.ttf",
        times_italics = "https://github.com/DocBox12/msfonts/raw/master/timesi.ttf",
        verdana = "https://github.com/DocBox12/msfonts/raw/master/verdana.ttf",
        verdana_bold = "https://github.com/DocBox12/msfonts/raw/master/verdanab.ttf",
        verdana_italics = "https://github.com/DocBox12/msfonts/raw/master/verdanai.ttf",
        verdana_italics_bold = "https://github.com/DocBox12/msfonts/raw/master/verdanaz.ttf"
    )

    font_url = DICT_fonts.get(font_name)

    currently_path = os.path.join(os.path.dirname(__file__))

    wget_exe = "cd " + currently_path + " && wget -c " + font_url

    os.system(wget_exe)

    return