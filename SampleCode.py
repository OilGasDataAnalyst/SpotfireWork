##########################################################
#working code!

from System.IO import Path, File, StreamWriter
from Spotfire.Dxp.Application.Visuals import TablePlot #CrossTablePlot

#Temp file for storing the cross table data
tempFolder = Path.GetTempPath()
tempFilename = Path.GetTempFileName()

#Export CrossTable data to the temp file
writer = StreamWriter(tempFilename)

#vTable1 2, & 3 are set up as "script parameters" see screen shot
vTable1.As[CrossTablePlot]().ExportText(writer)
vTable2.As[CrossTablePlot]().ExportText(writer)
vTable3.As[CrossTablePlot]().ExportText(writer)

print tempFilename

##########################################################
##########################################################
##########################################################
##########################################################
#what I'd like to do

from System.IO import Path, File, StreamWriter
#from Spotfire.Dxp.Application.Visuals import CrossTablePlot
from Spotfire.Dxp.Application.Visuals import *

#Temp file for storing the cross table data
#aware that I'd need to get diff file names for each so no 
#need to deal with this
tempFolder = Path.GetTempPath()
tempFilename = Path.GetTempFileName()

for p in Document.Pages: #loop through the pages
    for v in p.Visuals:  #loop through each visual
        if (v.TypeId != VisualTypeIdentifiers.HtmlTextArea 
            and v.TypeId != VisualTypeIdentifiers.MapChart2): #make sure they are not maps 
				viz = v.As[VisualContent]() #want to set the viz here!! 
				#then want to replicate the working code above... 
				writer = StreamWriter(tempFilename)
				#problem seems to occur here... I can already tell that I'm not setting
				#up the viz variable correctly... 
				viz.As[CrossTablePlot]().ExportText(writer) 