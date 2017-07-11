flickr_data = open('flickr_logos_27_dataset_training_set_annotation.txt', 'r') 



flag = False
arr_flic = []
flickr_data_namestest = open('/home/sumit/out_labels.txt', 'r')


chhm = 0
total = 0
for i in flickr_data_namestest:
        total += 1
        flickr_data_test = open('flickr_logos_27_dataset_query_set_annotation.txt', 'r')
	for j in flickr_data_test:
	     
             if i.split('/')[-1].split('.jpg')[0].strip() == j.split('.jpg')[0].strip() and i.split('/')[-1].split('.jpg')[-1].strip() == j.split('.jpg')[-1].strip():
		chhm += 1
		#print chhm
		#print "first:", i.split('/')[-1].split('.jpg')[0].strip(), j.split('.jpg')[0].strip()
             	#print "second:", i.split('/')[-1].split('.jpg')[-1].strip(), j.split('.jpg')[-1].strip()
        flickr_data_test.close()
#print total
print "accuracy:", float(chhm*100/total)
