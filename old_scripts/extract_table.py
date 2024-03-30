import tabula       # python package tabula-py
import jpype

#jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=F:\\Java\\bin\\java.exe", "-Djava.library.path=F:\\Java\\bin\\server\\jvm.dll")
# Path to the PDF file containing the table
pdf_path = "./price_list/1710916263.pdf"

# Extract tables from the PDF
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Iterate through each extracted table
for i, table in enumerate(tables, start=1):
    print(f"Table {i}:")
    print(table)
    print("\n")
