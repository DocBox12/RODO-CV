#!/usr/bin/env python3

# MAINTAINER

# Author: DocBox12
# Webpage: http://aboutme.morfiblog.pl/

import os
from fpdf import FPDF
import PyPDF3
import configparser
import fonts.fonts_manager
import argparse
import updater
import install

VERSION = "1.1-alpha"

def createpdf(default):
    check_version_and_news()
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
    new_file_cv_name = config['Default']['new_file_cv_name']

    LOWER_font_text = font_text.lower()

    font_ttf = fonts.fonts_manager.get_font(LOWER_font_text)
    
    path = os.path.join(os.path.dirname(__file__))
    full_font = path + "/fonts/" + font_ttf

    if default is False:
        with open(rodo_txt, 'r') as rt:
            rodo = rt.read()
    else:
        rodo = default_enclosure()

    pdf = FPDF(format=document_format, orientation = "P")
    pdf.l_margin = int(maring_left)
    pdf.add_page()
    pdf.add_font(font_text, '', full_font, uni=True)
    pdf.set_font(font_text, "", size=int(font_size))
    pdf.multi_cell(int(margin_right),int(line_spacing), txt=str(rodo), align=align_font)
    
    pdf.output(os.path.join(os.path.dirname(__file__), "temp.pdf"))

    temp_pdf_path = (os.path.join(os.path.dirname(__file__), "temp.pdf"))

    merge_pdf(temp_pdf_path, new_file_cv_name)

    return 

def merge_pdf(temp_pdf, new_cv):

    new_cv_path = os.path.join(os.path.dirname(__file__), new_cv)

    cv_path = os.path.join(os.path.dirname(__file__), 'cv.pdf')
    if not os.path.exists(cv_path):
        print("Nie znalazłem pliku cv.pdf. Skopiuj swoje CV do folderu aplikacji i uruchom program ponownie.")
        exit()


    LIST_pdf = [cv_path, temp_pdf]

    new_pdf = PyPDF3.PdfFileMerger() 

    for page in LIST_pdf:
        with open(page, 'rb') as f:
            new_pdf.append(f)

    with open(new_cv_path, 'wb') as f:
        new_pdf.write(f)
        print("Wygenerowałem CV")

    exit()

def default_enclosure():
    enclosure = "Wyrażam zgodę na przetwarzanie danych osobowych zawartych w niniejszym dokumencie do realizacji obecnego procesu rekrutacyjnego zgodnie z ustawą z dnia 10 maja 2018 roku o ochronie danych osobowych (Dz. Ustaw z 2018, poz. 1000) oraz zgodnie z Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (RODO)."
    
    
    return enclosure

def check_version_and_news():
    update = updater.check_update(VERSION)
    if update is not None:
        print(update)

    news = updater.news()
    if news is not None:
        print(news)

    return

def run_upgrade():
    updater.check_version(VERSION)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--default", help="Dodaje domyślną klauzurę RODO do CV pomijając tekst podany w pliku.", action="store_true")
    args = parser.parse_args()
    

    if args.default:
        createpdf(True)

    createpdf(False)