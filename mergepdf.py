# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 16:50:41 2019

@author: rayde
"""

#geektechstuff
#Python script to merge multiple PDF files into one PDF

#Requires the “PyPDF2” and “OS” modules to be imported
import os, PyPDF2

#Ask user where the PDFs are
userpdflocation= Downloads

#Sets the scripts working directory to the location of the PDFs
os.chdir(userpdflocation)

#Ask user for the name to save the file as
userfilename=input(‘What should I call the file?’)

#Get all the PDF filenames
pdf2merge = []
for filename in os.listdir(‘.’):
if filename.endswith(‘.pdf’):
pdf2merge.append(filename)

pdfWriter = PyPDF2.PdfFileWriter()

#loop through all PDFs
for filename in pdf2merge:
#rb for read binary
pdfFileObj = open(filename,’rb’)
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#Opening each page of the PDF
for pageNum in range(pdfReader.numPages):
pageObj = pdfReader.getPage(pageNum)
pdfWriter.addPage(pageObj)
#save PDF to file, wb for write binary
pdfOutput = open(userfilename+’.pdf’, ‘wb’)
#Outputting the PDF
pdfWriter.write(pdfOutput)
#Closing the PDF writer
pdfOutput.close()

