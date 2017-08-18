import wx
import wx.grid
import numpy as np
import wx.grid as gridlib

import matplotlib.pylab as plt
from scipy.stats import linregress

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent, Data):
        wx.grid.Grid.__init__(self, parent, -1)
        DiesMeasured         = Data[0]
        Waveguidelengths     = Data[1]
        self.PowerValues     = Data[2]
        Losses               = Data[3]
        R2_Fit_Values        = Data[4]
		
        if len(self.PowerValues)> len(Waveguidelengths):
			self.CreateGrid(len(self.PowerValues)+5, len(DiesMeasured)+1) #+5 for the analysis(space, WG loss, R2 value, Average loss, Std), +1 for the WG lengths
        else:
			self.CreateGrid(len(Waveguidelengths)+5, len(DiesMeasured)+1) #+5 for the analysis(space, WG loss, R2 value, Average loss, Std), +1 for the WG lengths
		#create table header
        #self.SetColLabelValue(0, "WG len(cm)")	
        self.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.onDragSelection)
        dieTrack = 0	
        for i in range(0, len(DiesMeasured)):
			self.SetColLabelValue(0, "X-param")	
			self.SetColLabelValue(i+1, "P(dBm) \n "+str(DiesMeasured[i]))
        #fill in raw data
        for Die in range(0,len(DiesMeasured)):
			WGlength = 0
			LongestColumn = 0		
			for power in range(0, len(self.PowerValues[Die])):
				self.SetRowLabelValue(0, "1")
				self.SetCellValue(power, Die+1, str(self.PowerValues[Die][power]))
				if WGlength+1 <= len(Waveguidelengths):
					self.SetCellValue(WGlength, 0, str(Waveguidelengths[WGlength]))
					WGlength+=1
				else:
					print "Number of waveguides do not match power values"
				LongestColumn+=1
					
        #fill in analyzed data
        parameters = ["Losses (dfu)", "R2 fit value", "Average", "Std. devia..."]

        for i in range(0, len(parameters)):
			LongestColumn+=1
			self.SetCellValue(LongestColumn, 0, str(parameters[i]))
        for Die in range(0, len(DiesMeasured)):
			R2_Fit_Values
			self.SetCellValue(LongestColumn-3, Die+1, str(Losses[Die]))
			self.SetCellValue(LongestColumn-2, Die+1, str(R2_Fit_Values[Die]))
			self.SetCellBackgroundColour(LongestColumn-3, Die+1, wx.GREEN)
			self.SetCellBackgroundColour(LongestColumn-2, Die+1, wx.GREEN)
        self.SetCellValue(LongestColumn-1, 1, str(round(np.average(Losses), 4)))
        self.SetCellValue(LongestColumn, 1, str(round(np.std(Losses),4)))
        self.SetCellBackgroundColour(LongestColumn-1, 1, wx.RED)
        self.SetCellBackgroundColour(LongestColumn, 1, wx.RED)
        
    def onDragSelection(self, event):
        """
        Gets the cells that are selected by holding the left
        mouse button down and dragging
        """
        if self.GetSelectionBlockTopLeft():
            top_left = self.GetSelectionBlockTopLeft()[0]
            bottom_right = self.GetSelectionBlockBottomRight()[0]
            self.printSelectedCells(top_left, bottom_right)
            
    def printSelectedCells(self, top_left, bottom_right):
        """
        Based on code from http://ginstrom.com/scribbles/2008/09/07/getting-the-selected-cells-from-a-wxpython-grid/
        """
        cells = [] 
        rows_start = top_left[0]
        rows_end = bottom_right[0] 
        cols_start = top_left[1]
        cols_end = bottom_right[1] 
        rows = range(rows_start, rows_end+1)
        cols = range(cols_start, cols_end+1) 
        cells.extend([(row, col)
            for row in rows
            for col in cols]) 
        #print "You selected the following cells: ", cells 
        self.NumberOfSelectedColumns = self.SelectedColumns(cells)
        self.SelectedData = [[0]*len(self.PowerValues)]*self.NumberOfSelectedColumns

        cnt = 0
        for i in range(0, len(cells)/2):
			for j in range(0, self.NumberOfSelectedColumns):
				#print cells[cnt], cells[cnt+1]
				#print self.GetCellValue(cells[cnt])
				cnt+=2
        for cell in cells:			
            row, col = cell
            #print self.GetCellValue(row, col)
            
    def SelectedColumns(self, cells):
		NumberOfSelectedColumns = 0
		temp = 0
		#This loop determines how many columns are selected from the table
		for i in range(0, len(cells)):
			if cells[i][1] >= temp:
				temp = cells[i][1] 
				NumberOfSelectedColumns+=1
			else:
				temp=len(cells)*2
			if NumberOfSelectedColumns == len(cells):
				NumberOfSelectedColumns = 1
		SelectedData = [[0]*len(self.PowerValues)]*NumberOfSelectedColumns

		if NumberOfSelectedColumns == 1:
			x_variable = [0]*(len(cells)/NumberOfSelectedColumns)	
			temp_col = [0]*(len(cells)/NumberOfSelectedColumns)
			cnt= 0 #cells[0][0]
			for cell in cells:			
				row, col = cell			
				temp_col[cnt]   = self.GetCellValue(row, col)
				x_variable[cnt] = self.GetCellValue(cnt+cells[0][0], 0)		
				cnt+=1		
			SelectedData = temp_col
			
			if  len((np.array(SelectedData))) > 1:
				for i in range(0, NumberOfSelectedColumns):
					slope = round((linregress((np.array(x_variable).astype(float)), (np.array(SelectedData)).astype(float)))[0], 4)
					r2val = round((linregress((np.array(x_variable).astype(float)), (np.array(SelectedData)).astype(float)))[2], 4) 
					plt.plot(x_variable, SelectedData,'p-', label="Slope: "+str(slope)+"::  R2 value "+str(r2val), hold=True)
				plt.legend(loc='best')
				plt.xlabel("WG number")
				plt.ylabel("Power levels [au]")
				plt.title("MMI losses")
				plt.show()								
		elif NumberOfSelectedColumns>=2: 
			start_col  = cells[0][1]
			staat_row  = cells[0][0]
			temp_col = [0]*(len(cells)/NumberOfSelectedColumns)	
			x_variable = [0]*(len(cells)/NumberOfSelectedColumns)	
					
			for col in range(0, NumberOfSelectedColumns):
				temp_col = [0]*(len(cells)/NumberOfSelectedColumns)
				for row in range(0, len(cells)/NumberOfSelectedColumns):
					#print self.GetCellValue(row, col)
					temp_col[row] = self.GetCellValue(row+staat_row, col+start_col)
					x_variable[row] = self.GetCellValue(row+staat_row, 0)
			#	print col+start_col
				SelectedData[col] = temp_col
			#SelectedData[0] = self.x_variable
			if  len((np.array(SelectedData))) > 1:
				if start_col==0:
					for i in range(0, NumberOfSelectedColumns-1):
						slope = round((linregress((np.array(SelectedData[0]).astype(float)), (np.array(SelectedData[i+1])).astype(float)))[0], 4)
						r2val = round((linregress((np.array(SelectedData[0]).astype(float)), (np.array(SelectedData[i+1])).astype(float)))[2], 4) 
						plt.plot(SelectedData[0], SelectedData[i+1],'p-', label="Slope: "+str(slope)+"::  R2 value "+str(r2val), hold=True)
				else:
					for i in range(0, NumberOfSelectedColumns):
						slope = round((linregress((np.array(x_variable).astype(float)), (np.array(SelectedData[i])).astype(float)))[0], 4)
						r2val = round((linregress((np.array(x_variable).astype(float)), (np.array(SelectedData[i])).astype(float)))[2], 4) 
						plt.plot(x_variable, SelectedData[i],'p-', label="Slope: "+str(slope)+"::  R2 value "+str(r2val), hold=True)
					
				plt.legend(loc='best')
				plt.xlabel("WG number")
				plt.ylabel("Power levels [au]")
				plt.title("MMI losses")
				plt.show()
		return NumberOfSelectedColumns
            
class TestFrame(wx.Frame):
    def __init__(self, parent, Data):
        wx.Frame.__init__(self, parent, -1, "Measurement data: 2b replaced by wafer name!",
                size=(560, 350), pos=(100,300))
        grid = SimpleGrid(self, Data)


