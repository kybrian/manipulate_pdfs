import os
from PyPDF2 import PdfFileReader

# Create a folder to store the split PDFs
output_folder = "split_pdfs"
os.makedirs(output_folder, exist_ok=True)

# Open the PDF file
pdf_file = "input.pdf"
pdf = PdfFileReader(pdf_file)

# Split the PDF into individual pages
for page_num in range(pdf.getNumPages()):
    # Get the page at the specified page number
    page = pdf.getPage(page_num)
    
    # Create a new PDF file for each page
    output_pdf = f"{output_folder}/page_{page_num + 1}.pdf"
    with open(output_pdf, "wb") as output:
        output_pdf.write(page)
    
    print(f"Page {page_num + 1} saved as {output_pdf}")

print("PDF split complete!")