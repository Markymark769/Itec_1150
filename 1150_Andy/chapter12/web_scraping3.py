#! python 3
"""
Mark Porraz, 5/6/2023, Web_scraping3
/ITEC 1150-90

Al Sweigart Automate book Chapter 11
original name: web_scraping_lab_v2.py
 This program downloads a webpage, extracts a poem, saves the file, re-opens the file and displays its contents

 This program does what I originally wanted, which is to web scrape the poem "Do Not Go Gentle Into That Good Night"
    using BeautifulSoup. - which would've been much easier had I kept up on my HTML.

    I also generalized it more than the last rushed program so that the web scrape and extract are now two different functions
    along with correcting my variable names to lower case and making the file function names more fitting.
    I also changed the file save mode from write binary to just plain write.
"""

import requests
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
            if str_input == "y" or str_input == "yes":  # an if statement for validation
                print("\n### Displaying raw html ###")  # display the website input
                print("\n", imported_webpage)
                print("\n###   End of raw html   ###")
                break
            elif str_input == "n" or str_input == "no":  # attempt to display the text from the raw txt
                print("\n### Displaying as written html ###")
                print('\n', str_filename)
                print("\n### End of written html ###")
                break
            else:
                print("Invalid input. Please try again.")  # validation for not putting valid html
        restart = input('Continue? Enter y or n: ')
        if restart == 'y':
            print('OK, let\'s get another Website.')
            main()
        else:
            print('Thanks for using the program.')
        # Extract text
        str_text = ExtractText(imported_webpage)
        # Export
        ExportFile(str_text, str_filename)
        # Re-import file
        print("\nSave complete, re-importing file.")
        str_content = ImportFile(str_filename)
        # Display contents of file on screen
        print("\nFile read into memory, displaying contents:\n")
        Display(str_content, str_filename)
    except Exception as err:  # usually displays when selecting no, needs work
        print("\nCongratulations. You broke the time continuum. Internal error\n")
        print(err)



def GetWebpage(str_url):
    # Get web page
    page_html = requests.get(str_url)
    # Parse with BeautifulSoup's html parser
    page_soup = soup(page_html.text, "html.parser")
    # Return result in soup format
    return page_soup


def ExtractText(page_soup):
    # Locate div tag, class - 'text_body'
    found = page_soup.find("div", {"class": "text_body"})
    # This strips all the leading white space from each paragraph
    text = '\n'.join(line.strip() for line in found.p.text.split('\n'))
    # Return parsed text as string
    return text


def ExportFile(str_content, str_filename):
    # Open specified file in write mode  (not write - binary like the last one)
    export_file = open(str_filename, 'w')
    # Write contents out to file
    export_file.write(str_content)
    # Close file
    export_file.close()
    # In a more complex program I'd have it return a result such as success/fail


def ImportFile(str_filename):
    # Open specified file in read mode
    import_file = open(str_filename, 'r')
    # Read contents of file in variable
    str_content = import_file.read()  # read file contents into variable
    # Close file
    # import_file.close   - not necessary to disabled
    return str_content


def Display(content, str_filename):
    # Pretty simple, display contents of file. It's already formatted correctly
    open(content, 'w')
    with open(str_filename, 'w', encoding='utf-8') as file:  # opens the file name input in write mode
        file.write(str_filename)
# encoding='utf-8' - character encoding when reading or writing contents of the file.
# Engage


if __name__ == '__main__':
    main()

# The stupid program doesn’t work because it there needs to be validation for turning the raw html into text.
# Because the function explicitly is for retrieving html, we run into complications in retrieving the html
# for validation while extracting the text from the raw data of  html.

