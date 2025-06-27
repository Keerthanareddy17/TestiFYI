from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    image = Image.open(image_path).convert('RGB')
    text = pytesseract.image_to_string(image)
    return text.strip()