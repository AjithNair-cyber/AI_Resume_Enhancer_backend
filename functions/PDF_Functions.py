import fitz

def extract_text_from_pdf(pdf_path):
   doc = fitz.open(pdf_path)  # open the PDF file
   response = ""
   for page in doc: # iterate the document pages
        text = page.get_text()# get plain text (is in UTF-8)
        response += text  # write text of page # write page delimiter (form feed 0x0C)
   doc.close()  # close the document
   return response
   


def generate_resume_from_html(html_content):

    # Create a new PDF document
    download_new = fitz.open()

    # Add a new page to the document
    page = download_new.new_page()

    # Define a bounding box (x0, y0, x1, y1) where the HTML will be inserted
    # This example uses a box covering most of the page, adjust as needed
    bbox = [50, 50, page.rect.width - 50, page.rect.height - 50]

    # Insert the HTML content into the specified bounding box
    page.insert_htmlbox(bbox, html_content)

    # Save the new document
    download_new.save("new_resume.pdf")