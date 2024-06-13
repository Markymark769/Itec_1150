
import requests, html2text
from bs4 import BeautifulSoup as soup


def main():
    # Set source URL where text is located.
    while True:
        str_url = input('Please paste in website: ')
        try:
            response = requests.head(str_url)
            if response.status_code == 200:
                break
            else:
                print('Invalid URL. Please try again.')
        except:
            print('Invalid URL. Please try again.')
    # Set filename
    str_filename = input('Please write file name in filename.txt format: ')
    # set filename to save contents to

    try:
        # Display status messages
        print("\nDownloading text from URL: ", str_url)
        print("Saving to                : ", str_filename)
        # Get specified webpage in soup html parsed format
        imported_webpage = GetWebpage(str_url)
        # Ask user if they'd like to see the source html
        while True:
            str_input = input("\nWould you like to see the unprocessed HTML? (y/n) : ")
            if str_input == "y" or str_input == "yes":
                print("\n### Displaying raw html ###")
                print("\n", imported_webpage)
                print("\n###   End of raw html   ###")
                break
            elif str_input == "n" or str_input == "no":
                print("\n### Displaying as written html ###")
                print(ExtractText(imported_webpage, raw=False))
                print("\n### End of written html ###")
                break
            else:
                print("Invalid input. Please try again.")
        # Extract text
        str_text = ExtractText(imported_webpage)
        # Export
        ExportFile(str_text, str_filename)
        # Re-import file
        print("\nSave complete,

