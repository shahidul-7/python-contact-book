from PyPDF2 import PdfMerger

AllPDF = ["pdf/bd-rail.pdf", "pdf/islami-akida.pdf"]

OurPdfMerger = PdfMerger()

for newpdf in AllPDF:
    OurPdfMerger.append(newpdf)

OurPdfMerger.write("ticket-book-combined.pdf")
OurPdfMerger.close()

