'''
@author Vivek Vikram Singh
@date 08.09.2017
Program to Unzip all files and create separate folder for each zip file with same name in same directory.
IT IS ONLY TESTED FOR ZIP FILES ONLY. OTHER ARCHIVE FORMATS SUCH AS TAR, GZ etc ARE NOT SUPPORTED.
Input: Directory name where all your zip files are kept.
Output: Each zip file has corresponding extracted folders.

'''
import os
import sys
import zipfile

root_dir = raw_input("Enter the directory path : ")
for curr_dir, sub_dirs, files in os.walk(root_dir):
	#print "Current Directory is : ", curr_dir
	for file_item in files:
		file_name = os.path.join(curr_dir, file_item)
		folder_name, extension = os.path.splitext(file_name)
		if extension == '.zip':
			if not os.path.exists(folder_name):
				print 'Extracting ',file_name
				os.mkdir(folder_name, 0755)	#create a folder with same name as zip file name except zip extension
				zip_ref = zipfile.ZipFile(file_name, 'r')
				zip_ref.extractall(folder_name)			
				zip_ref.close()
			else:
				print 'Already extracted ',file_name
