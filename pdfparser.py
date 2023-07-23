import tabula
from PyPDF2 import PdfReader

def extract_tabular_data(input_file_path):
    try:
        pdf_reader = PdfReader(input_file_path)
        total_pages = len(pdf_reader.pages)

        for curr_page in range(total_pages):
            # Read the current page
            page = pdf_reader.pages[curr_page]

            # Extracting text
            page_text = page.extract_text()

            # Use tabula-py to extract tabular data from the page
            tables = tabula.read_pdf(input_file_path, pages=curr_page + 1, lattice=True, multiple_tables=True)

            # Process the extracted tables on the current page
            for table_num, df in enumerate(tables, start=1):
                # Printing our DataFrame along with current page number and table contents
                print(f"Extracted tabular data from Table {table_num} on page {curr_page + 1}:")
                print(df)
                print("\n" + "=" * 30 + "\n")

    except FileNotFoundError:
        print(f"File not found or Invalid path: {input_file_path}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    # Specify the path to the PDF file
    inputfile = "input.pdf"

    extract_tabular_data(inputfile)

