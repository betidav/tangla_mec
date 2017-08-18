import os
from numpy import loadtxt

class MilabMeasurementTypes:
	def __init__(self):
		e = 2.71828183	
		self.measurementTypes = []
		
	def MType(self, path):
		filename = r""+str(path)			
		f = open(filename, 'r')
		x = f.readlines()
		for i in x:
			self.measurementTypes.append(i[0:len(i)])
		return  self.measurementTypes

#if __name__ == "__main__":
#	A = MilabWafers()
#	C = A.Wafers()
#	print C
