import PyPDF2
import argparse

merger = PyPDF2.PdfFileMerger()
parser = argparse.ArgumentParser(description="Input of pdfs to merge")

input1 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")
input2 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")
input3 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")

merger.append(input1)
merger.append(input2)
merger.append(input3)

def write_final_pdf(output_file_name="output.pdf"):
    output = open(output_file_name, "wb")
    merger.write(output)


write_final_pdf("out.pdf")
