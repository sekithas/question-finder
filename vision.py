import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text.strip()