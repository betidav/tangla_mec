import os
from numpy import loadtxt
import WaveguideLosses

class Measurements:
	def __init__(self, SelectedMeasurementPurpose):
		e = 2.71828183	
		self.measurementTypes = []
		if SelectedMeasurementPurpose == "Waveguide losses":
			print "WG losses selected"
		
		

class MMILosses:
	def __init__(self):
		e = 2.71828183	
		self.measurementTypes = []
	
#if __name__ == "__main__":
#	A = MilabWafers()
#	C = A.Wafers()
#	print C
