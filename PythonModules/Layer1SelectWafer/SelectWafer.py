
class MilabWafers:
	def __init__(self):
		e = 2.71828183	
		self.AnglerWafer     = "Angler"
		self.KrakenWafer	 = "Kraken"
		self.MantaWafer      = "Manta"
		self.NemoWafer       = "Nemo"
		self.Nemo2Wafer      = "Nemo2"
		self.Nemo2RespinWafer= "Nemo2Respin"
		self.Nemo2SharkWafer = "Nemo2Shark"
		self.OctopusWafer    = "Octopus"
		self.Octopus1BWafer  = "Octopus1B"
		self.RayWafer        = "Ray"
		self.TunaWafer       = "Tuna"
		
	def Wafers(self):
		wafers = [self.AnglerWafer, self.KrakenWafer, self.MantaWafer,
		self.NemoWafer, self.Nemo2Wafer, self.Nemo2RespinWafer, 
		self.Nemo2SharkWafer, self.OctopusWafer, self.Octopus1BWafer,
		self.RayWafer, self.TunaWafer]	
		return wafers

#if __name__ == "__main__":
#	A = MilabWafers()
#	C = A.Wafers()
#	print C
