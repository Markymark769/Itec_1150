import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
url = 'https://xkcd.com/'

def downloadNewestXkcd():
    print('Checking for new comic...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the newest comic
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
        return

    comicUrl = comicElem[0].get('src')
    comicNum = int(os.path.basename(comicUrl).replace('comic', '').replace('.png', ''))

    # Check if the newest comic has been downloaded
    if comicNum > getLatestComicNum():
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get('https:' + comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100):
            imageFile.write(chunk)
        imageFile.close()

        print('Comic %s downloaded.' % (comicNum))
    else:
        print('No new comic available.')

def getLatestComicNum():
    files = os.listdir('xkcd')
    if not files:
        return 0
    latestComicFile = max(files, key=lambda x: int(x.replace('comic', '').replace('.png', '')))
    return int(os.path.basename(latestComicFile).replace('comic', '').replace('.png', ''))


# create and start the Thread objects
downloadThreads = []  # a list of all the Thread objects
downloadThread = threading.Thread(target=downloadNewestXkcd)
downloadThreads.append(downloadThread)
downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')
