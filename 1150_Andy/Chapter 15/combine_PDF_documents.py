"""
Mark Porraz
combinePDFs.py
this program combines all the PDFs in the current working directory into a
single pdf
"""
import PyPDF2, os

pdfFile1 = open('meetingminutes.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')
pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)
pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)
pdfWriter = PyPDF2.PdfFileWriter()

# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
# pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFilesObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFilesObj)
    # Loop through all the pages (except the first) and add them.

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file
pdfOutput = open('Combinedminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

