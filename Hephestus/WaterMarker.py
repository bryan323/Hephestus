import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from WaterMark import*


class WaterMarker:

    def __init__(self, fileToWrite, fileToRead):
	self.fileToWrite = fileToWrite
	self.blankSheet = PdfFileReader(file(fileToRead, "rb"))



    def merge(self, newSheet):

	output = PdfFileWriter()

	page = self.blankSheet.getPage(0)

	page.mergePage(newSheet.getPage(0))

	output.addPage(page)

	outputStream = file(self.fileToWrite, "wb")
	output.write(outputStream)
	outputStream.close()

WM = WaterMark("Suck it nerd", 40, 688)
W2 = WaterMark("Eat My Shorts", 40, 712)

w = WaterMarker("Destination.pdf", "2404.pdf")


w.merge(WM.writeMark())
w.merge(W2.writeMark())
