# pdfmerger

A simple python based command line utility to merge and split PDF files.

## Installation

Use the package manager pip to install pdfmerger

```bash
pip3 install https://github.com/SarthakSharma2199/pdfmerger.git
```

## Usage

```python
pdfmerger file1.pdf[1, 2, 4-8] , file2.pdf[3-7]
#use [1, 2] to specify particular pages, or [4-8] for entire range
#you can also use the combination of the two.


pdfmerger file1.pdf[1, 2, 4-8] , file2.pdf[3-7] -o myfile.pdf
#default output is to the file output.pdf
#to specify the output file name, use -o argument

```



## License
[MIT](https://choosealicense.com/licenses/mit/)