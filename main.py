from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs = []
n = int(input("Enter the number of PDF files to merge: "))
for i in range(0,n):
    name = input(f"Enter the name of PDF file {i+1}: ")
    merger.append(name)

# Merging the PDF files
for pdf in pdfs:
    merger.append(pdf)


merger.write("merged-pdf.pdf")
merger.close()