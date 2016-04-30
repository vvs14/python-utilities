'''
@author Vivek Vikram Singh
@date 26.03.2016
Program to Delete all image files in given Directory and all of its sub directories.
To input correct directory path : go to that directory, right click on any file and see the path. Give that path in input.
Can be used to remove images from a directory where images are not required among all other files.

'''
import os
from os.path import exists
import time
import imghdr

root_dir = raw_input("Enter the directory path : ")
for curr_dir, sub_dirs, files in os.walk(root_dir):
	print "Current Directory is : ", curr_dir
	time.sleep(1)
	for file_item in files:
		fname = os.path.join(curr_dir,file_item)
		img_type = imghdr.what(fname)
		if os.path.exists(fname):
			if img_type:
				print "Deleting : ",fname
				os.remove(fname)
			else:
				print fname ," is not Image file."
		else:
			print "File does not exist"

