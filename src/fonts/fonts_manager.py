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
        verdana_idalics = "verdanai.ttf",
        verdana_idalics_bold = "verdanaz.ttf"
    )

    font_ttf = DICT_fonts.get(font_name)

    return font_ttf
