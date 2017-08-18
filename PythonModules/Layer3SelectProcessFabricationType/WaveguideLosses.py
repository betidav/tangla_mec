import os
from numpy import loadtxt

class WaveguideLosses:
	def __init__(self):
		e = 2.71828183	
		self.measurementTypes = []
		
	def WaveguidEtchDefinition(self, path):
		filename = r""+str(path)			
		f = open(filename, 'r')
		x = f.readlines()
		for i in x:
			self.measurementTypes.append(i[0:len(i)])
		return  self.measurementTypes
		
	def WaveguideTopClad(self, path):
		return null
	
	def WaveguideOpenCladEtch(self, path):
		return null
	
	def OxideRedepositionAfterOpenCladEtch(self, path):
		return null

class MMILosses:
	def __init__(self):
		e = 2.71828183	
		self.measurementTypes = []
	
#if __name__ == "__main__":
#	A = MilabWafers()
#	C = A.Wafers()
#	print C
