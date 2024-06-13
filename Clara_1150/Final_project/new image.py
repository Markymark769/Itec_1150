from base64 import b64decode

import docx
import requests
from io import BytesIO
from docx import Document
from docx.shared import Inches

response = requests.get('https://national-parks-1150.azurewebsites.net/api/OLYM').json()

park_image = content['nps_park_images']
binary_img = BytesIO(response.content)
print(park_image)
park_word_document = docx.Document()
park_word_document.add_picture('nps_park_images', width=Inches(2))
park_word_document.save('park_image.docx')


