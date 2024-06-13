import webbrowser, requests, bs4
import sys, pyperclip

# webbrowser.open('http://inventwithpython.com/')
# webbrowser.open('https://minneapolis.edu/')

import webbrowser, pyperclip
place = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + place)