import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class WaterMark():
 
    def __init__(self, mark, x, y):

	self.location = {"X": x, "Y" : y}
	self.mark = mark
	self.packet = StringIO.StringIO()
	self.canvas = canvas.Canvas(self.packet, pagesize = letter)

    def getLocation(self, locationCoords):

	return self.location[locationCoords]

    def writeMark(self):
        self.canvas.drawString(self.getLocation("X"), self.getLocation("Y"), self.mark)
        self.canvas.save()

	self.packet.seek(0)
        self.new2404 = PdfFileReader(self.packet)
	return self.new2404
 
	

