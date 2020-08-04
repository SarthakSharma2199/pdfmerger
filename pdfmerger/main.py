import PyPDF2
import argparse
import re

merger = PyPDF2.PdfFileMerger()
parser = argparse.ArgumentParser(description="Input of pdfs to merge")

def write_final_pdf(output_file_name):
    output = open(output_file_name, "wb")
    merger.write(output)

def append_pdf_selectively(pdf_file, from_page_num, to_page_num):
    pdf_file=open(pdf_file, "rb")
    merger.append(fileobj=pdf_file, pages=(from_page_num, to_page_num))

def append_pdf(pdf_file):
    pdf_file = open(pdf_file, "rb")
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
    check_extension=output_file_name.split('.')
    if(check_extension[1]!="pdf"):
        output_file_name=check_extension[0]+".pdf"



args.pdf_array = [i for i in args.pdf_array if i !=',']
print(args.pdf_array)

for i in args.pdf_array:
    print(i)
    check_file_name_regex="/(^.+[.pdf]{1}([\[]{1}[\]]{1}$)?)/"
    pdf_name=re.search("(^.+(.pdf){1})", i)

    if(pdf_name):
        pdf_name=pdf_name.group(1)

    #if there is no page argument
    if (re.search("((.pdf){1}$)", i)):
        append_pdf(pdf_name)
        #print("yes")

    else:
        page_array=re.search("([\[]{1}.+[\]]{1}$)", i)
        if(page_array):
            page_array=page_array.group(1)
        #print(page_array)




#Calling write function
write_final_pdf(output_file_name)
