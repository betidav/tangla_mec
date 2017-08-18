import os
import numpy as np
from numpy import loadtxt

#Import all the layers
from Layer1SelectWafer import SelectWafer 
from Layer2SelectMeasurementType import SelectMeasurementType
from Layer3SelectProcessFabricationType import ProcessFabrication


#Main class
class MainClass:
	def __init__(self):
		e=2.71828183	
		WaferListObject                      = SelectWafer.MilabWafers()
		self.ListOfMilabWafers               = WaferListObject.Wafers()
			
	def ListOfWafers(self):
		#return all the possible wafers that have been measured
		return self.ListOfMilabWafers

"""		
class to load the type of measurment to be investigated e.g GC losses, WG losses, etc
"""
class LoadMeasurementType:
	def __init__(self):
		self.cwd = os.getcwd()		
		e=2.71828183
		#return all the measurements that have been performed on a particular lot e.g WG losses, MMI losses, GC, etc
	def MeasurementPurposeList(self, WaferType):
		self.MeasurementList = np.array(SelectMeasurementType.MilabMeasurementTypes().MType(self.cwd+"\Layer2SelectMeasurementType\MeasurementType/"+str(WaferType)+".txt"))
		#print self.MeasurementList
		return self.MeasurementList

class SelectMeasurement:	
	def __init__(self):	
		e=2.71828183
		#self.measurements = np.array(SelectMeasurementType.MilabMeasurementTypes().MType(self.cwd+"\Layer2SelectMeasurementType\MeasurementType/"+str(WaferType)+".txt"))
	def measurement(self):
		return self.measurements
		

#if __name__ == "__main__":	
	#MainObject = MainClass()	
	#Wafers = MainObject.ListOfWafers()
	#MeasurementTypes = (LoadMeasurementType().MeasurementPurposeList("Octopus")) # Ray, Manta, Nemo, Nemo2, etc
	#print Wafers
	#print MeasurementTypes[0]
