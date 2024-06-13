"""
Mark Porraz, 11/21/2023, Web Scraping part 3
Beautiful Soup -- BS4
Automate the Boring Stuff
Chapter 12: Web Scraping
"""
# download Beautiful Soup -- BS4
# pip install beautifulsoup4

import requests, bs4
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
bs4.BeautifulSoup
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)
bs4.BeautifulSoup
