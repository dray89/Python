from docx import Document

files = []
for i in range(1, 6):
    files.append("dray\\Documents\\Projects\\Proj-41861-P"+str(i)+"-Debra.docx")

    def combine_word_documents(files):
        merged_document = Document()

 # Don't add a page break if you've reached the last file.
        for index, file in enumerate(files):
            sub_doc = Document(file)
            if index < len(files)-1:
               sub_doc.add_page_break()
       
            for element in sub_doc.element.body:
                merged_document.element.body.append(element)

        merged_document.save("dray\\Documents\\Projects\\Duke_Interviews_41861.docx")

    combine_word_documents(files)