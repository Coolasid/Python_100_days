from pypdf import PdfWriter
import os

x = [a for a in os.listdir('./mypdfs') if a.endswith('.pdf')]
print(f"==>> x: {x}")

merger = PdfWriter()

for pdf in x:
    merger.append(open(os.path.join('./myPdfs',pdf), 'rb'))


with open(os.path.join('./mergedPdf',"result.pdf"), "wb") as fout:
    merger.write(fout)