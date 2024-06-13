import requests
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/POODLE')
res.raise_for_status() # 200 or 400?

soup = BeautifulSoup(res.text, 'html.parser')
paragraphs = soup.find('h1').get_text()
text = soup.get_text(separator=' ')

with open('POODLE.txt', 'w', encoding='utf-8') as file:
    file.write(text)



# import requests
# res = requests.get('https://en.wikipedia.org/wiki/POODLE')
# res.raise_for_status()
# playFile = open('POODLE.txt', 'wb')
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)