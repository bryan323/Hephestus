from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = StringIO.StringIO()

can = canvas.Canvas(packet, pagesize = letter)
can.drawString(10, 10, "940876")
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)

existing_pdf = PdfFileReader(file("2404.pdf", "rb"))
output = PdfFileWriter()

page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

outputStream = file("PAS-13E(V)3.pdf", "wb")
output.write(outputStream)
outputStream.close()
 
