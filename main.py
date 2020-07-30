import PyPDF2
import argparse

merger = PyPDF2.PdfFileMerger()
parser = argparse.ArgumentParser(description="Input of pdfs to merge")

def write_final_pdf(output_file_name):
    output = open(output_file_name, "wb")
    merger.write(output)

def append_pdf_selectively(pdf_file, from_page_num, to_page_num):
    merger.append(fileobj=pdf_file, pages=(from_page_num, to_page_num))

def append_pdf(pdf_file):
    merger.append(pdf_file)

#setting default name for output file
output_file_name="output.pdf"

#First argument contains the name of the pdfs to be merged and the range of pages
help_text_1="Add pdf names to the argument, eg.  file1.pdf[1-4] , file2.pdf[3, 4-6]\n"
parser.add_argument("pdf_array", nargs="+", help=help_text_1)

#Optional argument for setting output file name
parser.add_argument("--output", "-o",  help="Name of output pdf")

#object of parsed arguments
args=parser.parse_args()

#setting custom output file name if it is supplied
if(args.output):
    output_file_name=args.output
    print(output_file_name)

print(args.pdf_array)


input1 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")
input2 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")
input3 = open("PDF_Samples/AutoCad_Diagram.pdf", "rb")

merger.append(input1)
merger.append(input2)
merger.append(input3)




#Calling write function
write_final_pdf(output_file_name)
