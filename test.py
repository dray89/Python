import os, docx, keyword, untangle
from xml.sax import make_parser, handler
obj = untangle.parse("Program Evaluation_Memo.xml")
doc = docx.Document()
para = doc.add_paragraph(str(obj))
doc.save("doc")