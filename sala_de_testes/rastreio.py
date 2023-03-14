from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from sys import argv

#chatgpt generated
import requests
import pytesseract
from PIL import Image

# download captcha image
url = 'https://example.com/captcha.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# preprocess image
img = img.convert('L')  # convert to grayscale
img = img.point(lambda x: 0 if x < 128 else 255, '1')  # binarize image

# solve captcha
captcha_text = pytesseract.image_to_string(img)

print(captcha_text)
