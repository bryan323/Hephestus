from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class StandardInfo:

    def __init__(self, organization, nomenclature,
                     serial, date, inspectionType, tmNumber, tmDate,
                     inspectorName, timeOfInspection):

        self.info = {"Organization":organization, "Nomenclature":nomenclature, "Serial":serial, "Date":date, 
		     "Inspection Type":inspectionType, "TM Number" : tmNumber, "TM Date":tmDate, "Inspector Name":inspectorName,
		     "Time Of Inspection":timeOfInspection}

    def getProperty(self, property):

        return self.info[property]


