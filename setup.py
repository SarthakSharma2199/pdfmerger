from setuptools import setup

setup(
    name='pdfmerger',
    version='0.0.1',
    description='A simple python based command line utility to merge and split PDF files.',
    url='https://github.com/SarthakSharma2199/pdfmerger',
    author='Sarthak Sharma',
    author_email='sarthaksharma2199@outlook.com',
    license='MIT',
    install_requires=['PyPDF2'],
    packages=["pdfmerger"],
    entry_points={
            'console_scripts': [
                'pdfmerger = pdfmerger.main:start_script'
            ]
    }

)