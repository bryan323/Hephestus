import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from WaterMark import*


class WaterMarker:

    def __init__(self, x, y, mark, fileToWrite, fileToRead):
	
	self.fileToWrite = fileToWrite
	self.mark = mark
	self.x = x
	self.y = y
	self.packet = StringIO.StringIO()
	self.canvas = canvas.Canvas(self.packet, pagesize = letter)
	self.blankSheet = PdfFileReader(file(fileToRead, "rb"))
	

    def writeAndMerge(self):
	self.canvas.drawString(self.x, self.y, self.mark)
	self.canvas.save()

	self.packet.seek(0)
	newSheet = PdfFileReader(self.packet)
	
	output = PdfFileWriter()

	page = self.blankSheet.getPage(0)

	page.mergePage(newSheet.getPage(0))

	output.addPage(page)

	outputStream = file("New 2404.pdf", "wb")
	output.write(outputStream)
	outputStream.close()
	
 
WM = WaterMark("Suck it Nerds", 10, 10)


marker = WaterMarker(WM.getLocation("X"), WM.getLocation("Y"), WM.getMark(), "Destination.pdf", "2404.pdf")

marker.writeAndMerge()
