import webbrowser, pyperclip, requests

# webbrowser.open('http://minneapolis.edu')
# opens in default browser

# run this with a place name in the clipboard such as Bad Bergzabern, Germany
# place = pyperclip.paste() # paste the copied address
# webbrowser.open('https://www.google.com/maps/place/' + place)

# 2) web_scraping1.py - write a program to download a .txt file from online, open and read
# the file, and then display the output. Note: you do NOT have to display the whole file or write
# to a .txt file (optional). Step 1 – find a .txt file online to work with, other than the example.
# The example program downloads, opens and reads a file, hosted at this address:

# Alice in Wonderland on Project Gutenberg https://www.gutenberg.org/files/11/11-0.txt
URL="https://www.gutenberg.org/files/11/11-0.txt"
response = requests.get(URL)
filename = "alice.txt"

with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.content.decode('utf-8'))
file.close()

readfile = open(filename, 'r', encoding='utf-8')
readfile_line = readfile.readline()
line_count = 1
while ((readfile_line) and (line_count < 140)):
    print(readfile_line)
    readfile_line = readfile.readline()
    line_count = line_count + 1
readfile.close()
print("that's all for now!")



