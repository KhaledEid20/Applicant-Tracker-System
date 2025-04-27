
import pdfplumber
def read_pdf(file_path):
    """
    Reads a PDF file and returns its text content.
    
    Args:
        file_path (str): The path to the PDF file.
        
    Returns:
        str: The text content of the PDF file.
    """
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text