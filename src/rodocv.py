#!/usr/bin/env python3

import os
from fpdf import FPDF
import PyPDF3
import configparser
import fonts.fonts_manager

def createpdf():
    # Loading config
    config = configparser.ConfigParser()
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')

    rodo_txt = os.path.join(os.path.dirname(__file__), 'klauzura.txt')
    config.read(config_file)

    document_format = config['Default']['document_format']
    font_text = config['Default']['font_text']
    font_size = config['Default']['font_size']
    align_font = config['Default']['align_font']

    font_ttf = fonts.fonts_manager.get_font(font_text)

    with open(rodo_txt, 'r') as rt:
        rodo = rt.read()


    pdf = FPDF(format=document_format, orientation = "P")
    pdf.l_margin = 5
    pdf.r_margin = 100
    pdf.add_page()
    pdf.add_font(font_text, '', font_ttf, uni=True)
    pdf.set_font(font_text, "", size=int(font_size))
    pdf.multi_cell(200,5, txt=rodo, align=align_font)
    
    pdf.output("temp.pdf")




    return

if __name__ == "__main__":
    createpdf()