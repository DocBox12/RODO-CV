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
    maring_left = config['Default']['maring_left']
    margin_right = config['Default']['margin_right']
    line_spacing = config['Default']['line_spacing']

    font_ttf = fonts.fonts_manager.get_font(font_text)

    with open(rodo_txt, 'r') as rt:
        rodo = rt.read()


    pdf = FPDF(format=document_format, orientation = "P")
    pdf.l_margin = int(maring_left)
    pdf.add_page()
    pdf.add_font(font_text, '', font_ttf, uni=True)
    pdf.set_font(font_text, "", size=int(font_size))
    pdf.multi_cell(int(margin_right),int(line_spacing), txt=str(rodo), align=align_font)
    
    pdf.output("temp.pdf")

    merge_pdf("temp.pdf")

    return 

def merge_pdf(temp_pdf):
    LIST_pdf = ["cv.pdf", temp_pdf]

    new_pdf = PyPDF3.PdfFileMerger() 

    for page in LIST_pdf:
        with open(page, 'rb') as f:
            new_pdf.append(f)

    with open("moje_cv.pdf", 'wb') as f:
        new_pdf.write(f)

    return

if __name__ == "__main__":
    createpdf()