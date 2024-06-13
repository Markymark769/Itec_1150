"""
Mark Porraz, 11/21/2023, Web Scraping part 1
Automate the Boring Stuff
Chapter 12: Web Scraping
"""
# for downloading Romeo and Juliet
# example 1) This is done in the console
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

# res.status_code == requests.codes.ok
# len(res.text)
# print(res.text[:250])

# this is pretty much all it does
# just opens a web browser