#Import modules to be used
import os,sys
import shutil
#Import image file, Background and plot them

class fileAndFolderNamesInDirectory:
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
		
	def folderNames(self, path):
		arrayOfNames = []
		"""
		This function returns all the foldernames in a given directory
		"""
		try:
			subdirectories = os.listdir(path)
			print subdirectories
			for i in range(0, len(subdirectories)):
				if os.path.isdir(path +"/"+ subdirectories[i]):				
					arrayOfNames.append(subdirectories[i])
				else:
					print "done directoring!"
		except Exception, e:
			print "Error reading folder names ", e, 'for more info....info@tanglatec.com'
		return arrayOfNames
		
	def copyFilesFromA2B(self, source, destination):
		files = os.listdir(source)
		count = 1
		for file in files:
			try:		
				shutil.copy(source+str(file),destination+str(file))
				count+=1
			except Exception, e:
				print "Error reading file names: Check detination folder to see if all files have been copied", 
				e, 'for more info....info@tanglatec.com'
	def createNewFolder(self, path):
		try:
			os.mkdir(path, 0777) #0777, 7=full admin right, 7=read/write permission, 7=read/execute permission
			"""
				os.mkdir(path[, mode])--> path = path to be created, mode--> mode of the directories to be given
			"""
		except Exception, e:
			print "Error reading file names: Check detination folder to see if all files have been copied", 
			e, 'for more info....info@tanglatec.com'
			
	def openFileInITsDefaultExtension(self, path):
		file = "C:\\Documents\\file.txt"
		os.startfile(file)

def func():
	A = fileAndFolderNamesInDirectory()
	#name = A.folderNames(r"\\nt4\milab\WP3 LFI\photonics\SQUID-miLFI_01\sweep\03-05-2017\Set1/")
	name = A.folderNames(r"E:\Kinyuy\Octopus\WG_losses\After_Waveguide_etch_definition/Raw data")
	print name
func()
