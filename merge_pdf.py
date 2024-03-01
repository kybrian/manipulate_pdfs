import os
from PyPDF2 import PdfFileMerger

# Create a new folder to store the output
output_folder = "merged_pdfs"
os.makedirs(output_folder, exist_ok=True)

# Get the list of PDF files in the "outputs" folder
pdf_folder = "split_pdfs"
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

# Sort the PDF files based on their names
pdf_files.sort(key=lambda x: int(x.split(".")[0]))

# Merge the PDF files
merger = PdfFileMerger()
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    merger.append(pdf_path)

# Save the merged PDF to the output folder
output_path = os.path.join(output_folder, "merged.pdf")
merger.write(output_path)
merger.close()

print("PDFs merged successfully!")