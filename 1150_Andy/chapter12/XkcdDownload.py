"""
Mark Porraz, 11/21/2023, Web Scraping part 4
Xkcd Comics
- This program downloads free and open source comics
from:
Automate the Boring Stuff
Chapter 12: Web Scraping
"""

# import requests, os, bs4

import requests, os, bs4

url = 'https://xkcd.com'               # starting url, start by specifying the URL as a variable
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd, create a directory
while not url.endswith('#'):  # we then loop all over the different comics
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')  # we use beautiful soup on the various pages

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')  # we are going to call select on soup (method ---> isnumeric)
# we are going to get the comic image
    if comicElem == []:  # if there is no image
        print('Could not find comic image.')  # we print could not find
    else:  # if the image does exist
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd folder that is created.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')  # creating a file
        for chunk in res.iter_content(1000):
            imageFile.write(chunk)  # writing the image file
        imageFile.close()  # always good practice to close a file

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]  # we are going to get the link
    url = 'https://xkcd.com' + prevLink.get('href')  # appending to the prev link
print('Done')
