"""
Mark Porraz
encrypting PDF documents
5/9/2024

this is supposed to be the syntax for encrypting PDF documents,
It usually should go in the python console.
"""

import PyPDF2
pdfFile = open('meetingminutes.pdf', 'rb')  # Create variable pdfFile and open the pdf file in read binary
pdfReader = PyPDF2.PdfFileReader(pdfFile)  # Create variable pdfReader and use the PyPDF2 library with the read function
# to open the pdf file that is referenced in the variable
pdfWriter = PyPDF2.PdfFileWriter()  # Create variable pdfWriter and use the PyPDF2 library with the write function
# to write what we desire

for pageNum in range(pdfReader.numPages):  # we are passing a loop to get the number of pdf pages
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')  # we are using the encrypted message as a password for the PDF document
# users need this password to access this document

resultPdf = open('encryptedminutes.pdf', 'wb')

pdfWriter.write(resultPdf)

resultPdf.close()




