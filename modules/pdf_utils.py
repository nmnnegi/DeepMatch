import base64
import io
import fitz  # PyMuPDF
from PIL import Image

def extract_pdf_image_and_text(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf_doc:
        first_page = pdf_doc[0].get_pixmap()
        img_byte_arr = io.BytesIO(first_page.tobytes("jpeg"))
        text = ""
        for page in pdf_doc:
            text += page.get_text()
        return (
            Image.open(img_byte_arr),
            base64.b64encode(img_byte_arr.getvalue()).decode(),
            text,
        )
