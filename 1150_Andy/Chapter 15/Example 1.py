"""
Mark Porraz
Working with PDFs and word Documents

note: be sure that you download the pyPDF2 module
*the previous version 1.2.6 is really the only thing that works with this
* yes, this is a ways from the most current version, do this at the beginning of chapter for
better results (downgrade)
"""
# when file loaded, we need ot change the current working directory
# C:\Users\marky\PycharmProjects\1150_Andy\Chapter 15
# import PyPDF2
# pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdfReader.numPages
# expected output: 19
# this here is returning the number of pages in a PDF document


# pageObj = pdfReader.getPage(0)
# pageObj.extractText()
# here we are returning the text that is found in the text document
# expected output:
# 'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '
# pdfFileObj.close()  # note after we are done, we need to ensure that we are closing our file

# import PyPDF2
# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# pdfReader.isEncrypted
# expected output: True
#

# >>> pdfReader.getPage(0) --->>> this should fail

#pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# pdfReader.decrypt('rosebud')
# 1
# pageObj = pdfReader.getPage(0)



