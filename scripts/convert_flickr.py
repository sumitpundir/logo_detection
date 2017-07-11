import scipy.misc
from PIL import Image
import xml.etree.cElementTree as ET
import os

##open the training data
flickr_data = open('flickr_logos_27_dataset_training_set_annotation.txt', 'r') 

##creating train set
flick_data_names = open('/home/sumit/flickr_logos_27_dataset/ImageSets/train.txt', 'a')

##mapping classes to corresponding labels
dict_flick = {'Adidas': 1, 'Apple': 2, 'BMW': 3, 'Citroen': 4, 'Cocacola': 5, 'DHL': 6, 'Fedex': 7, 'Ferrari': 8, 'Ford': 9, 'Google': 10, 'Heineken': 11, 'HP': 12, 'McDonalds': 13, 'Mini': 14, 'Nbc': 15, 'Nike': 16, 'Pepsi': 17, 'Porsche': 18, 'Puma': 19, 'RedBull':20, 'Sprite': 21, 'Starbucks':22, 'Intel':23, 'Texaco':24, 'Unicef':25, 'Vodafone':26, 'Yahoo':27}

flag = False

arr_flic = []
 		
##creating .xml files Annotation and train.txt file ImageSets from training dataset.
for i in flickr_data:
    arr_flickr = i.split(' ')
    flag = False
    chhm += 1
    filename = arr_flickr[0].split('.')[0].strip()+".xml" 
    if os.path.isfile("/home/sumit/flickr_logos_27_dataset/xml_files/"+filename):
    	tree = ET.parse("/home/sumit/flickr_logos_27_dataset/xml_files/"+filename)
    	root = tree.getroot()
    	image_location = "/home/sumit/flickr_logos_27_dataset/flickr_logos_27_dataset_images/"+str(arr_flickr[0])
    	img = Image.open(image_location)
    	width, height = img.size
    	doc = ET.SubElement(root, "object")
    	ET.SubElement(doc, "name").text = str(dict_flick[str(arr_flickr[1])])
    	ET.SubElement(doc, "truncated").text = str(0)
    	ET.SubElement(doc, "difficult").text = str(0)
    	val = ET.SubElement(doc, "bndbox")
    	ET.SubElement(val, "xmin").text = str(arr_flickr[3])
    	ET.SubElement(val, "ymin").text = str(arr_flickr[4])
    	ET.SubElement(val, "xmax").text = str(arr_flickr[5])
    	ET.SubElement(val, "ymax").text = str(arr_flickr[6])
    	tree = ET.ElementTree(root)
    	filename = arr_flickr[0].split('.')[0].strip()+".xml"
    	tree.write("/home/sumit/flickr_logos_27_dataset/xml_files/"+filename)
    	flag = True
    	continue
	if flag == True:
		continue
    image_location = "/home/sumit/flickr_logos_27_dataset/flickr_logos_27_dataset_images/"+str(arr_flickr[0])
    print >> flick_data_names, arr_flickr[0].split('.')[0].strip()
    print "true:"
    img = Image.open(image_location)
    width, height = img.size
    root = ET.Element("annotation")
    ET.SubElement(root, "filename").text = str(arr_flickr[0].split('.')[0].strip())
    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(width)
    ET.SubElement(size, "height").text = str(height)
    ET.SubElement(size, "depth").text = str(3)
    doc = ET.SubElement(root, "object")
    ET.SubElement(doc, "name").text = str(dict_flick[str(arr_flickr[1])])
    ET.SubElement(doc, "truncated").text = str(0)
    ET.SubElement(doc, "difficult").text = str(0)
    val = ET.SubElement(doc, "bndbox")
    ET.SubElement(val, "xmin").text = str(arr_flickr[3])
    ET.SubElement(val, "ymin").text = str(arr_flickr[4])
    ET.SubElement(val, "xmax").text = str(arr_flickr[5])
    ET.SubElement(val, "ymax").text = str(arr_flickr[6])
    tree = ET.ElementTree(root)
    filename = arr_flickr[0].split('.')[0].strip()+".xml"
    tree.write("/home/sumit/flickr_logos_27_dataset/xml_files/"+filename)

flick_data_names.close()
flickr_data.close()

