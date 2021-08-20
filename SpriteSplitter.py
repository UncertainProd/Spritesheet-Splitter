import xml.etree.ElementTree as ET
from PIL import Image
from sys import argv

name = argv[1] # Eg: BOYFRIEND
file_base_name = argv[2] if len(argv) > 2 else None

imagepath = name+".png"
xmlpath = name + ".xml"

im = Image.open(imagepath)
xml_tree = ET.parse(xmlpath)

CATEGORY_NAME = "SubTexture"

coord_sets = xml_tree.findall(CATEGORY_NAME)
coord_list = []

for i, obj in enumerate(coord_sets):
	print("Getting spriteNum: ", i)
	x1 = int(obj.get('x'))
	y1 = int(obj.get('y'))
	w = int(obj.get('width'))
	h = int(obj.get('height'))
	posename = obj.get('name')
	if (x1, y1) not in coord_list:
		im1 = im.crop((x1, y1, x1+w, y1+h))
		save_name = f"{file_base_name}-{i}.png" if file_base_name else f"{name}-{posename}-{i}.png"
		im1.save(save_name)
		coord_list.append((x1, y1))