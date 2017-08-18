import os
import numpy as np
from numpy import loadtxt
import shutil
#Import image file, Background and plot them

class FolderNamesInDirectory:		
	def folderNames(self, path):
		arrayOfNames = []
		"""
		This function returns all the foldernames in a given directory
		"""
		try:
			subdirectories = os.listdir(path)
			for i in range(0, len(subdirectories)):
				if os.path.isdir(path +"/"+ subdirectories[i]):				
					arrayOfNames.append(subdirectories[i])
				else:
					#print "done directoring!"
					Nothing = "nothing"
		except Exception, e:
			print "Error reading folder names ", e, 'for more info....info@tanglatec.com'
		return arrayOfNames

class fileNamesInDirectory:
	def fileNames(self, path):
		files = os.listdir(path)
		"""
		This function returns an array of all the filenames in the specified path. Note that the 
		last element in the returned array maybe a 'Thumbs.db' file
		"""
		arrayOfNames = []
		for file in files:
			try:
				arrayOfNames.append(file)
			except:
				print 'error last file, # ', count, 'file', 'for more info....info@tanglatec.com'
		return arrayOfNames
