import xml.etree.ElementTree as ET
import os

current_path = os.getcwd()
files = os.listdir(current_path)

for f in files:
    if f.startswith("znalezione"):
        full_path = os.path.join(current_path, f)
        os.remove(full_path)

def get_xml_file_list():
    file_list=[]
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".xml")]:
            file_list.append(os.path.join(dirpath, filename))
    return file_list
	

with open('ppe.txt','r') as f:
    ppe_nums = f.read().split()

file_list = get_xml_file_list()

for xml_name in file_list :
	print(xml_name)
	ET.register_namespace('',"http://www.companysite.pl/gudk/0.10")
	tree= ET.parse(xml_name)
	root=tree.getroot()

	zestawienie=root.find('{http://www.companysite.pl/gudk/0.10}Zestawienie')
	if zestawienie is not None:
		root.remove(zestawienie)
	dokumenty=root.find('{http://www.companysite.pl/gudk/0.10}Dokumenty')

	rozliczenia=dokumenty.findall('{http://www.companysite.pl/gudk/0.10}Dokument')

	found = []
	
	for doc in rozliczenia:
		dane_ppe=doc.find('{http://www.companysite.pl/gudk/0.10}DanePPE')
		nr_ppe=dane_ppe.find('{http://www.companysite.pl/gudk/0.10}NrPPE').text
		typ = doc.find('{http://www.companysite.pl/gudk/0.10}Typ').text
		if nr_ppe in ppe_nums and (typ == 'FR' or typ == 'FK'):
			found.append(nr_ppe)
		else:
			dokumenty.remove(doc)
	
	if found != []:
		nry_ppe = ''
		for nr_ppe in found:
			nry_ppe = nry_ppe + '_' + nr_ppe
		tree.write('znalezione'+os.path.basename(xml_name),encoding="UTF-8",xml_declaration=True)

		

