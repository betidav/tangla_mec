#  MAINGUI.py
#  
#  Copyright 2017 kongny41 <kongnyuy>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import wx
import wx.animate
import os, sys, time
import traceback
import numpy as np
import importlib
from PIL import Image
#from Main import MainClass
import imp
#from Main import LoadMeasurementType
from PythonModules import Data2Table#, LoadData2Data2Table
from PythonModules.local_functions import FolderNames
#from "PythonModules\local_functions" import FolderNames

    
class GeneralCalls:
	def __init__(self, path):
		e=2.71828183
		#path = path.replace('.', '/')
		#print path
		instance= imp.load_source('measurementfile', path+'/measurementfile.py')


		Data =instance.Measurements().Returndatafunc()
		Waveguidelengths     = Data[0]		
		PowerValues          = Data[1]
		DiesMeasured         = Data[2]
		Losses               = Data[3]
		R2_fit_values        = Data[4]
		
		Data = [DiesMeasured,Waveguidelengths,PowerValues, Losses, R2_fit_values]
		app2 = wx.PySimpleApp()
		frame2 = Data2Table.TestFrame(None, Data)
		frame2.Show(True)
		app2.MainLoop()
		
def show_error():
    message = ''.join(traceback.format_exception(*sys.exc_info()))
    dialog = wx.MessageDialog(None, message, 'Error!', wx.OK|wx.ICON_ERROR)
    dialog.ShowModal()
    			
class MyPanels(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent)
        self.parent = parent

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1130, 670),
            style=wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|
                  wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)
        #os.system("start C:\Users")
		
        self.st = 1
        self.horizontal_shift = 40
        self.vertical_shift   = 30
        self.initial_button_position = 10
        self.GeneralRequestsCalls = 4
        
        self.MeasurementPurpose_first_selection_layer2 = 0
        self.WaferSelection_combo_box_on               = True
        self.combopurposeMeasurementPurposeLayer2      = None
        
        self.parent = parent

        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour("grey")
        
        #define lefe and right pannels and give a background color
        self.leftpanel  = MyPanels(self.panel, 1)
        self.rightpanel = MyPanels(self.panel, 1)
        
        self.leftpanel.SetBackgroundColour("blue")
        self.rightpanel.SetBackgroundColour("black")

        self.basicsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.basicsizer.Add(self.leftpanel, 1, wx.EXPAND)
        self.basicsizer.Add(self.rightpanel, 1, wx.EXPAND)
        self.panel.SetSizer(self.basicsizer)
        #self.textbox = wx.TextCtrl(self.rightpanel, size=(500,-1), style=wx.CB_READONLY)
        #self.textbox.SetValue(''.join(map(str, "PNG image of size: w*h = 500x600")))


        #Add a menu bar ################################################################
        ################################################################################
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitMenuItem = fileMenu.Append(wx.NewId(), "Restart",
                                       "Restart application")
        exitMenuItem = fileMenu.Append(wx.NewId(), "About",
                                       "About the application")
        exitMenuItem = fileMenu.Append(wx.NewId(), "Help",
                                       "Help about the application")
        exitMenuItem = fileMenu.Append(wx.NewId(), "Exit",
                                       "Exit the application")
        menuBar.Append(fileMenu, "&File")
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
        self.Bind(wx.EVT_MENU, self.onHelpRequest, exitMenuItem)
        self.SetMenuBar(menuBar)        
        #End of menu bar###############################################################

        try:
			#self.ReshapeImage("images\wafers\wafer.png")			
			self.WaferType = wx.Button(self.leftpanel, 3, 'Layr1: Wafer', (self.initial_button_position+self.horizontal_shift,
																					  self.initial_button_position+self.vertical_shift),(115,25))
			self.WaferType.Bind(wx.EVT_BUTTON,self.WaferSelectionLayer1) 
			self.png = wx.StaticBitmap(self.rightpanel, 1, wx.Bitmap("images\wafers\wafer.png", wx.BITMAP_TYPE_ANY), (50,1))
			#gif_fname = "images\gui\tracer.gif"

        except Exception as e:
			print e
        
        #Centralized 
        self.Centre() 
        self.Show() 
        self.Fit()    

			
    def onExit(self, event):
        """"""
        self.Close()
    def onHelpRequest(self, event):
		""""""
		print "Tangla David, info@tanglatec.com"
 
    def CreateNewPanel(self, event, combo):
	
        self.rightpanel = MyPanels(self.panel, 1)
        self.rightpanel.SetBackgroundColour("sage")
        self.basicsizer.Add(self.rightpanel, 1, wx.EXPAND)
        self.panel.Layout()        
        self.Centre()
        self.Show(True)

    def destroyPanel(self, event):
        self.rightpanel.Hide()
        self.panel.Layout()

    def WaferSelectionLayer1(self, event):
        try: 
			
            """
            WaferSelectionLayer1 function selects all the wafers that are measured and placed in the photonics folder.
            """
            cwd = os.getcwd()	
            self.directory = cwd  
            self.dataPath = cwd
            self.WaferList= FolderNames.FolderNamesInDirectory().folderNames(cwd+"/Photonics")

			#self.WaferList                     = MainClass().ListOfWafers()        
            self.comboWaferSelectionLayer1     = wx.ComboBox(self.leftpanel,choices = self.WaferList, pos=wx.Point(self.initial_button_position+4*self.horizontal_shift,
																					  self.initial_button_position+self.vertical_shift), size=wx.Size(350, 150)) 
            self.comboWaferSelectionLayer1.SetToolTip(wx.ToolTip("select wafer name from list"))                
            self.comboWaferSelectionLayer1.Bind(wx.EVT_COMBOBOX, self.MeasurementPurposeLayer2)
            
            self.m_animCtrl1 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, (0,417 ), ( -1,-1 ), wx.animate.AC_DEFAULT_STYLE )
            self.m_animCtrl1.LoadFile( u"images\\gui\\tracer.gif" )
            self.m_animCtrl1.Play()            
        except Exception as e:
            print e
 
        
    def MeasurementPurposeLayer2(self, event):    
		try:
			self.combopurposeMeasurementPurposeLayer2.Hide()
			self.GeneralRequestsCalls = 4
			try:
				self.combofabricationprocess.Hide()
				try:
					self.combopurposeMeasurementPurposeLayer2.Hide()
					try:
						self.combofabricationprocess.Hide()
						try:
							self.comboGeneralRequest.Hide()
							try:
								self.comboIntermediateRequest.Hide()
								try:
									self.comboSemiFinalRequest.Hide()
								except:
									pass								
							except:
								pass							
						except:
							pass							
					except:
						pass					
				except:
					pass				
			except:
				pass	    
		except:
			pass
		try:
		    """
		    For each selected wafer, MeasurementPurposeLayer2 lists all the measurements that have been performed on that wafer
		    """
		    #self.comboWaferSelectionLayer1.Hide()
		    self.SelectedWafer     = str(self.comboWaferSelectionLayer1.GetStringSelection()).rstrip()       
		    self.textbox = wx.TextCtrl(self.leftpanel, size=(560,-1), style=wx.CB_READONLY)  
		    path =   (self.directory + str("/Photonics/")+  self.SelectedWafer)
		    self.dataPath = path
		    #self.ReshapeImage('images\gds/'+str(self.SelectedWafer)+'.png')	
		    self.MeasurementPurposeList = FolderNames.FolderNamesInDirectory().folderNames(path)

		    file = open(str(path)+"/"+"__init__.py","w") #write this file in the given path  to make path a python module
		    self.textbox.SetValue(self.dataPath)    

		    self.WaferType         = wx.Button(self.leftpanel, 3, 'Layr2: Measurements', (self.initial_button_position+self.horizontal_shift,
										self.initial_button_position+2*self.vertical_shift),(115,25))
										 
		    self.path2GdsOfWaferSelected = 'images\gds/'+str(self.SelectedWafer)+'.png'
		    if os.path.isfile(self.path2GdsOfWaferSelected):							 
				self.png.SetBitmap(wx.Bitmap(self.path2GdsOfWaferSelected)) 
     
		    self.combopurposeMeasurementPurposeLayer2      = wx.ComboBox(self.leftpanel,choices = self.MeasurementPurposeList, pos=wx.Point(self.initial_button_position+4*self.horizontal_shift,
																			self.initial_button_position+2*self.vertical_shift   ), size=wx.Size(350, 150))   
		    self.combopurposeMeasurementPurposeLayer2.SetToolTip(wx.ToolTip("select measurement purpose from list"))
		    self.combopurposeMeasurementPurposeLayer2.Bind(wx.EVT_COMBOBOX, self.MeasurementFabricationProcessLayer3)
		except Exception as e:
		    print show_error , e
        
    def MeasurementFabricationProcessLayer3(self, event): 
	
		try: 
			try:
				self.combofabricationprocess.Hide()
				try:
					self.combofabricationprocess.Hide()
					try:
						self.comboGeneralRequest.Hide()
						try:
							self.comboIntermediateRequest.Hide()
							try:
								self.comboSemiFinalRequest.Hide()
							except:
								pass								
						except:
							pass							
					except:
						pass							
				except:
					pass			
			except:
				pass				
			"""
            The fabrication processes for the device you selected is chosen at this point by MeasurementFabricationProcessLayer3
            """
			path = self.directory + str("/Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip()
			self.dataPath = path
			Files = FolderNames.fileNamesInDirectory().fileNames(path)
			file = open(str(path)+"/"+"__init__.py","w") #write this file in the given path  to make path a python module 
			if "measurementfile.py" in Files: 		
				if ('wafermap.PNG' in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/')):
					self.image = path+'\Raw data\wafermap.png'
					#self.ReshapeImage(self.image)
					subdirectories = os.listdir(path)
					self.png.SetBitmap(wx.Bitmap(self.image))
					GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip())
				else:
					self.png.SetBitmap(wx.Bitmap("images\wafers\wafer.png"))
					GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip())
													
			else:
				self.PowerPointOverView(path)			
				path = (self.directory + str("/Photonics/") +str(str(self.comboWaferSelectionLayer1.GetStringSelection()).rstrip() )+str("/") 
																					   +str(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() )
				
				self.textbox.SetValue(self.dataPath)  
				file = open(str(path)+"/"+"__init__.py","w") #write this file in the given path  to make path a python module			
				self.fabricationprocesses = FolderNames.FolderNamesInDirectory().folderNames(path)			
				self.FabricationProcess         = wx.Button(self.leftpanel, 3, 'Layr3: Process', (self.initial_button_position+self.horizontal_shift,
																				self.initial_button_position+3*self.vertical_shift),(115,25))  
				self.combofabricationprocess = wx.ComboBox(self.leftpanel,choices = self.fabricationprocesses, pos=wx.Point(self.initial_button_position+4*self.horizontal_shift,
																						  self.initial_button_position+3*self.vertical_shift   ), size=wx.Size(350, 150))  
				#print str(self.combofabricationprocess.GetStringSelection()).rstrip()  
				     
				self.combofabricationprocess.Bind(wx.EVT_COMBOBOX, self.GeneralRequests)
		except Exception, e:
			print show_error, self.MeasurementFabricationProcessLayer3.__doc__ , e
			
    def GeneralRequests(self, event):
		"""
		GeneralRequest checks if there is a measurement file in the directory: 
		"""
		try: 
			try:
				self.GeneralRequestsCalls= 4
				#self.combofabricationprocess.Hide()
				r = "nothing"
				try:
					#self.combofabricationprocess.Hide()
					r = "nothint"
					try:
						#self.comboGeneralRequest.Hide() 
						r = "nothing"
						try:
							self.comboIntermediateRequest.Hide()
							try:
								self.comboSemiFinalRequest.Hide()
							except:
								pass								
						except:
							pass							
					except:
						pass							
				except:
					pass			
			except:
				pass			
			path = (self.directory + str("/Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 	
																					   +("/")+ str(self.combofabricationprocess.GetStringSelection()).rstrip())
																					     
			self.dataPath = path
			Files = FolderNames.fileNamesInDirectory().fileNames(path)
			FoldersINPath = FolderNames.FolderNamesInDirectory().folderNames(path)
			file = open(str(path)+"/"+"__init__.py","w") #write this file in the given path  to make path a python module 
			if "measurementfile.py" in Files:
				try:
					"""wafer map if available else use default wafer map
					"""									
					if ('wafermap.PNG' in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/')):
						subdirectories = os.listdir(path)
						self.png.SetBitmap(wx.Bitmap(path+'\Raw data\wafermap.png'))
						GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																					  +("/")+ str(self.combofabricationprocess.GetStringSelection()).rstrip()) 						
					else:
						try:
							if "Structure.PNG" in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/'):
								self.png.SetBitmap(wx.Bitmap(path +'\Raw data\Structure.png'))
							else:
								self.png.SetBitmap(wx.Bitmap("images\wafers\wafer.png"))
						except:						
							pass								
						GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																					  +("/")+ str(self.combofabricationprocess.GetStringSelection()).rstrip()) 
	
				except Exception as e:
					print show_error, self.GeneralRequests.__doc__	 , e								
			else:	
				self.PowerPointOverView(path)	
				#path = self.directory + str("/Photonics/") +str(str(self.comboWaferSelectionLayer1.GetStringSelection()).rstrip() )+str("/") +str(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
				self.comboGeneralRequest = wx.ComboBox(self.leftpanel,choices = FoldersINPath, pos=wx.Point(self.initial_button_position+4*self.horizontal_shift,
																				  self.initial_button_position+4*self.vertical_shift   ), size=wx.Size(300, 150))
				self.GeneralRequestsCalls+=1												  	
				self.comboGeneralRequest.Bind(wx.EVT_COMBOBOX, self.IntermediateRequest)

		except Exception as e:
			print e	

    def IntermediateRequest(self, event):
		path = (self.directory + str("/Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																					+("/")+ str(self.combofabricationprocess.GetStringSelection()).rstrip() 
																					+ str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip()))
		self.dataPath = path
		Files = FolderNames.fileNamesInDirectory().fileNames(path)
		FoldersINPath = FolderNames.FolderNamesInDirectory().folderNames(path)		
		file = open(str(path)+"/"+"__init__.py","w") #write this file in the given path  to make path a python module 							  	
		#self.comboGeneralRequest.Bind(wx.EVT_COMBOBOX, self.CreateComboBox)
		if "measurementfile.py" in Files:
			try:
				try:
					self.GeneralRequestsCalls = 4
					#self.combofabricationprocess.Hide()
					self.comboSemiFinalRequest
					r = "nothing"
					try:
						#self.combofabricationprocess.Hide()
						r = "nothint"
						try:
							#self.comboGeneralRequest.Hide() 
							r = "nothing"
							try:
								#self.comboIntermediateRequest.Hide()
								r = nothing
								try:
									self.comboSemiFinalRequest.Hide()
								except:
									pass								
							except:
								pass							
						except:
							pass							
					except:
						pass			
				except:
					pass
				"""wafer map if available else use default wafer map
				"""									
				if ('wafermap.PNG' in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/')):
					subdirectories = os.listdir(path)
					self.png.SetBitmap(wx.Bitmap(path+'\Raw data\wafermap.png'))
					GeneralCalls(str("Photonics.") +(self.SelectedWafer)+str(".") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																				  +(".")+ str(self.combofabricationprocess.GetStringSelection()).rstrip() 	
																				  + str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip()))					
				else:					
					try:
						if "Structure.PNG" in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/'):
							self.png.SetBitmap(wx.Bitmap(path +'\Raw data\Structure.png'))
						else:
							self.png.SetBitmap(wx.Bitmap("images\wafers\wafer.png"))
					except:						
						pass
					GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() +("/")
																				  + str(self.combofabricationprocess.GetStringSelection()).rstrip()
																				  + str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip()))

			except Exception as e:
				print show_error, self.GeneralRequests.__doc__	 , e								
		else:	
			self.PowerPointOverView(path)	
			#path = self.directory + str("/Photonics/") +str(str(self.comboWaferSelectionLayer1.GetStringSelection()).rstrip() )+str("/") +str(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
			self.comboIntermediateRequest = wx.ComboBox(self.leftpanel,choices = FoldersINPath, pos=wx.Point(self.initial_button_position+4*self.horizontal_shift,
																			  self.initial_button_position+5*self.vertical_shift   ), size=wx.Size(300, 150))
			self.GeneralRequestsCalls+=1												  	
			self.comboIntermediateRequest.Bind(wx.EVT_COMBOBOX, self.SemiFinalRequest)	
	

    def SemiFinalRequest(self, event):
		
		path = (self.directory + str("/Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																					+("/")+ str(self.combofabricationprocess.GetStringSelection()).rstrip()
																					+ str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip())
																					+str("/")+ str((self.comboIntermediateRequest.GetStringSelection()).rstrip()))
		self.dataPath = path
		Files = FolderNames.fileNamesInDirectory().fileNames(path)
		FoldersINPath = FolderNames.FolderNamesInDirectory().folderNames(path)	
		file = open(str(path)+"/"+"__init__.py","w") #write this file in the given path  to make path a python module 								  	
		#self.comboGeneralRequest.Bind(wx.EVT_COMBOBOX, self.CreateComboBox)
		if "measurementfile.py" in Files:
			try:
				try:
					self.GeneralRequestsCalls = 4
					#self.combofabricationprocess.Hide()
					r = "nothing"
					try:
						#self.combofabricationprocess.Hide()
						r = "nothint"
						try:
							#self.comboGeneralRequest.Hide() 
							r = "nothing"
							try:
								#self.comboIntermediateRequest.Hide()
								r = nothing
								try:
									#self.comboSemiFinalRequest.Hide()
									r =  "nothing"
								except:
									pass								
							except:
								pass							
						except:
							pass							
					except:
						pass			
				except:
					pass
				"""wafer map if available else use default wafer map
				"""									
				if ('wafermap.PNG' in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/')):
					subdirectories = os.listdir(path)
					self.png.SetBitmap(wx.Bitmap(path+'\Raw data\wafermap.png'))
					GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() +("/")
																				 + str(self.combofabricationprocess.GetStringSelection()).rstrip()
																					+str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip())
																					+str("/")+ str((self.comboIntermediateRequest.GetStringSelection()).rstrip())) 																				  						
				else:
					try:
						if "Structure.PNG" in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/'):
							self.png.SetBitmap(wx.Bitmap(path +'\Raw data\Structure.png'))
						else:
							self.png.SetBitmap(wx.Bitmap("images\wafers\wafer.png"))
					except:						
						pass
					GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() +("/")
																					+ str(self.combofabricationprocess.GetStringSelection()).rstrip()
																					+str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip())
																					+str("/")+ str((self.comboIntermediateRequest.GetStringSelection()).rstrip())) 

			except Exception as e:
				print show_error, self.GeneralRequests.__doc__	 , e	
		else:	
			self.PowerPointOverView(path)	
			#path = self.directory + str("/Photonics/") +str(str(self.comboWaferSelectionLayer1.GetStringSelection()).rstrip() )+str("/") +str(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
			self.comboSemiFinalRequest = wx.ComboBox(self.leftpanel,choices = FoldersINPath, pos=wx.Point(self.initial_button_position+4*self.horizontal_shift,
																			  self.initial_button_position+6*self.vertical_shift   ), size=wx.Size(300, 150))
			self.GeneralRequestsCalls+=1												  	
			self.comboSemiFinalRequest.Bind(wx.EVT_COMBOBOX, self.FinalRequest)	
			
    def FinalRequest(self, event):
		path = (self.directory + str("/Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																					+("/")+ str(self.combofabricationprocess.GetStringSelection()).rstrip()
																					+ str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip())
																					+str("/")+ str((self.comboIntermediateRequest.GetStringSelection()).rstrip())
																					+str("/")+ str((self.comboSemiFinalRequest.GetStringSelection()).rstrip()))		
		self.dataPath = path
		Files = FolderNames.fileNamesInDirectory().fileNames(path)
		FoldersINPath = FolderNames.FolderNamesInDirectory().folderNames(path)	
		file = open(str(path)+"/"+"__init__.py","w") #write this file in the given path  to make path a python module 								  	
		#self.comboGeneralRequest.Bind(wx.EVT_COMBOBOX, self.CreateComboBox)
		if "measurementfile.py" in Files:
			try:
				"""wafer map if available else use default wafer map
				"""									
				if ('wafermap.PNG' in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/')):
					subdirectories = os.listdir(path)
					self.png.SetBitmap(wx.Bitmap(path+'\Raw data\wafermap.png'))
					GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																				+str("/")    + str(self.combofabricationprocess.GetStringSelection()).rstrip() 
																				+str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip())
																				+str("/")+ str((self.comboIntermediateRequest.GetStringSelection()).rstrip())
																				+str("/") + str((self.comboSemiFinalRequest.GetStringSelection()).rstrip())) 						
				else:
					try:
						if "Structure.PNG" in FolderNames.fileNamesInDirectory().fileNames(path+'\Raw data/'):
							self.png.SetBitmap(wx.Bitmap(path +'\Raw data\Structure.png'))
						else:
							self.png.SetBitmap(wx.Bitmap("images\wafers\wafer.png"))
					except:						
						pass					
					GeneralCalls(str("Photonics/") +(self.SelectedWafer)+str("/") +(self.combopurposeMeasurementPurposeLayer2.GetStringSelection()).rstrip() 
																					+str("/") + str(self.combofabricationprocess.GetStringSelection()).rstrip()
																					+str("/") + str((self.comboGeneralRequest.GetStringSelection()).rstrip())
																					+str("/")+ str((self.comboIntermediateRequest.GetStringSelection()).rstrip())
																					+str("/") + str((self.comboSemiFinalRequest.GetStringSelection()).rstrip())) 
						
			except Exception as e:
				print show_error, self.GeneralRequests.__doc__	 , e
		else:	
			print "No measurement file found"							
													
    def ReshapeImage(self, path):
		image = Image.open(path)
		image.thumbnail((400, 600), Image.ANTIALIAS)
		image.save(path, 'PNG', quality=88)
	
    def PowerPointOverView(self, path):
		if "Overview.PNG" in FolderNames.fileNamesInDirectory().fileNames(path):
			self.image = path+'\Overview.png'
			subdirectories = os.listdir(path)
			self.png.SetBitmap(wx.Bitmap(self.image))					

def main():
    app = wx.App()
    try:
        frame = MyFrame(None, -1, 'DataFynda Milab.py')
        frame.Show()
        app.MainLoop()
    except:
        show_error()

if __name__ == '__main__':
    main()
