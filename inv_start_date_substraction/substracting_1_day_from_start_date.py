# This code finds invoice start date and substracts one day from it so it can be uploaded with matching criteria.

import lxml.etree as ET
import os
import datetime

file_list = [f for f in os.listdir() if f.endswith(".xml")]

for xml_name in file_list:
    print(xml_name)
    tree = ET.parse(xml_name)
    root = tree.getroot()

    zestawienie = root.find('{http://www.website.pl/0.12}Zestawienie')
    dokumenty = root.find('{http://www.website.pl/0.12}Dokumenty')

    rozliczenie = dokumenty.find('{http://www.website.pl/0.12}Dokument')

    doc_rozliczenia = rozliczenie.find(
        '{http://www.website.pl/0.12}Rozliczenia')
    doc_rozliczenie = doc_rozliczenia.findall(
        '{http://www.website.pl/0.12}Rozliczenie')
    okres = rozliczenie.find('{http://www.website.pl/0.12}Okres')

    poczatek = okres.find('{http://www.website.pl/0.12}Poczatek').text
    print(f"Pierwotna data: {poczatek}")
    poczatek = datetime.datetime.strptime(poczatek, "%Y-%m-%d")
    delta = datetime.timedelta(1)
    poczatek_nowy = (poczatek - delta).date()
    poczatek = poczatek.strftime("%Y-%m-%d")
    poczatek_nowy = poczatek_nowy.strftime("%Y-%m-%d")
    print(f"Poprawiona data: {poczatek_nowy}")

    for elem in root.getiterator():

        try:
            elem.text = elem.text.replace(poczatek, poczatek_nowy)
        except AttributeError:
            pass
    tree.write('poprawiona_data_' + os.path.basename(xml_name),
               encoding="UTF-8", xml_declaration=True)
