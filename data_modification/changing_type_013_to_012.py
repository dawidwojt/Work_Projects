# This code modifies specific items in xml files to match with criteria specified to upload it into server.


import lxml.etree as ET
import os


file_list = [f for f in os.listdir() if f.endswith(".xml")]

for xml_name in file_list:
    print(xml_name)
    tree = ET.parse(xml_name)
    root = tree.getroot()
    go = True

    for elem in root.getiterator():

        try:
            elem.text = elem.text.replace('nr ', '')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace('Licznik energii', 'Energia czynna')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace(
                'Składnik stały stawki sieciowej', 'Opłata dystrybucyjna stała')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace(
                'Stawka opłaty przejściowej', 'Opłata przejściowa')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace(
                'Stawka jakościowa', 'Składnik jakościowy całodobowa')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace(
                'Składnik zmienny stawki sieciowej', 'Składnik sieciowy całodobowa')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace(
                'Opłata OZE', 'Opłata OZE całodobowa')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace(
                'Opłata kogeneracyjna', 'Opłata kogeneracyjna całodobowa')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace(
                'Stawka opłaty abonamentowej', 'Opłata abonamentowa')
        except AttributeError:
            pass
        try:
            elem.text = elem.text.replace('zł/mc', 'mc')
        except AttributeError:
            pass

    tree.write('poprawiona_wersja_' + os.path.basename(xml_name),
               encoding="UTF-8", xml_declaration=True)
