# pdfmerger

A simple python based command line utility to merge and split PDF files.

## Installation

Use the package manager pip to install pdfmerger

```bash
pip3 install git+https://github.com/SarthakSharma2199/pdfmerger.git
```

## Usage

```python

pdfmerger file1.pdf , file2.pdf , file3.pdf
#to append multiple pdfs together

pdfmerger file1.pdf[4-8] , file2.pdf[3-7]
#use [4-8] to specify the page range to be included from a pdf


pdfmerger file1.pdf[4-8] , file2.pdf[3-7] -o myfile.pdf
#default output is to the file output.pdf
#to specify the output file name, use -o argument

```



## License
[MIT](https://choosealicense.com/licenses/mit/)
