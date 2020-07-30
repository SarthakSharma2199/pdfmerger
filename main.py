import PyPDF2

merger=PyPDF2.PdfFileMerger()
input1 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")
input2 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")
input3 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")

merger.append(input1)
merger.append(input2)
merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)