# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:08:50 2019

@author: rayde
"""


# pdf_merging.py

from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def merge_pdfs(paths, output = 'C:\\Users\\rayde\\Documents\\merge_files\\OfferLetter.PDF'):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = []
    for file in os.listdir("C:\\Users\\rayde\\Documents\\merge_files"):
          if file.endswith(".pdf"):
               paths.append("C:\\Users\\rayde\\Documents\\merge_files\\"+ file)
    merge_pdfs(paths)