import requests, os, bs4, time

os.chdir(r'C:\Users\marky\PycharmProjects\chapter17')

comic = 1
url_image_num = 4980

def download_comic():
    global comic
    global url_image_num
    url = 'http://explosm.net/comics/' + str(url_image_num) + '/'
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match = soup.find('img', id='main-comic')
        comic_url = 'http:' + match.get('src')
        res = requests.get(comic_url)
        res.raise_for_status()
        print('Downloading C&H' + str(comic).zfill(4) + '...')
        image_file = open('C&H' + str(comic).zfill(4) + '.jpg', 'wb')
        for chunk in res.iter_content(100):
            image_file.write(chunk)
        image_file.close()
        comic += 1
        url_image_num += 1
        url = 'http://explosm.net/comics/' + str(url_image_num + 1) + '/'
        print(url)
    except requests.exceptions.HTTPError:
        print('No comic was found. Will try again in 8 hours')
    # I found the easiest way to make this program is to use time.sleep(1)
    # Put it in a for loop for however many seconds you want (28800 is 8 hours) and it will
    # complete after that time
    for second in range(28800):
        time.sleep(1)

# Another for loop controls the function itself. Since there are three 8-hour blocks in a day,
# 21 for loops will run for a week straight. You can set these numbers to whatever you want.
for hour_block in range(21):
    print('Searching for a new comic')
    download_comic()


