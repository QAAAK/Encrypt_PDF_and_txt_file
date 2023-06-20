from PyPDF2 import PdfFileReader, PdfFileWriter
from getpass import getpass
pdf_writer = PdfFileWriter()
pdf_reader = PdfFileReader('file.pdf')

for page in range(pdf_reader.numPages):
    pdf_writer.add_page(pdf_reader.pages[page])

password = getpass(prompt='Enter the password')
pdf_writer.encrypt(password)

with open('open_file.pdf','wb') as file:
    pdf_writer.write(file)


