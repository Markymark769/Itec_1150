# web_scraping3.py – start with the demo11_webscraping2.py file, and make improvements as follows:
# • Change the variable str_url so it is a user-supplied web address.
# • provide basic correction and validation of the input
# • Change the variable str_filename so it is dynamic, in keeping with the URL.
# • Hint: use part of the user-supplied str_url to construct a file name OR provide some other automated naming system.
# • Review what characters should and shouldn't be in a file name, so you can avoid or # remove those.
# • Add a restart feature to the program

# • When the above steps are complete, and the user enters 'y' to see raw html, the
# program should run until it gets to the ExtractPoem function. At that point, most # likely it will fail.
# • Add comments to the function, and use section 6 of the PDP to propose how the
# function would have to change to work with a new, user-defined request program.
# You do NOT have to implement the solution, but run some tests to inform your answer.

#! python 3
"""
Birch, Michael
ITEC 1150-90

Al Sweigart Automate book Chapter 11
original name: web_scraping_lab_v2.py
 This program downloads a webpage, extracts a poem, saves the file, re-opens the file and displays its contents

 This program does what I originally wanted, which is to web scrape the poem "Do Not Go Gentle Into That Good Night"
    using BeautifulSoup. - which would've been much easier had I kept up on my HTML.

    I also generalized it more than the last rushed program so that the web scrape and extract are now two different functions
    along with correcting my variable names to lower case and making the file function names more fitting.
    I also changed the file save mode from write binary to just plain write.
"""
from bs4 import BeautifulSoup as soup       # As soup so you don't have to keep typing BeautifulSoup
import requests
import re


def main():
    # Set source URL where poem is located.
    # str_url = "http://allpoetry.com/Do-Not-Go-Gentle-Into-That-Good-Night"
    match = False
    while not match:
        str_url = input("Please enter the URL: ")
        pattern = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$')
        # start: ^ end: $
        match = bool(re.match(pattern, str_url))

    print(str_url)

    # Set filename
    # str_filename = "DoNotGoGentle.txt"                                  # set filename to save contents to
    match = False
    while not match:
        str_filename = input("Please enter the desired filename: ")
        pattern = re.compile(r'^[\w\-]+\.[\w]+$')
        match = bool(re.match(pattern, str_filename))
        # note could create filename from the URL


    try:
        # Display status messages
        print("\nDownloading poem from URL: ", str_url)
        print("Saving to                : ", str_filename)
        # Get specified webpage in soup html parsed format
        imported_webpage = GetWebpage(str_url)
        # Ask user if they'd like to see the source html
        while True:
            str_input = input("\nWould you like to see the unprocessed HTML? (y/n) : ")  # Get user input
            if str_input == "y" or str_input == "yes":    # If yes display source html /// for some reason if I use .lower, it does not work.
                print("\n### Displaying raw html ###")
                print("\n", imported_webpage)
                print("\n###   End of raw html   ###")
                break
            elif str_input == "n" or str_input == "no":   # If no, then display nothing and continue on..
                break
            else:
                print("Invalid input. Please try again.") # If no matching option detected, display error message and ask again.
        # Extract Poem
        str_poem = ExtractPoem(imported_webpage)
        # Export
        ExportFile(str_poem, str_filename)
        # Re-import file
        print("\nSave complete, re-importing file.")
        str_content = ImportFile(str_filename)
        # Display contents of file on screen
        print("\nFile read into memory, displaying contents:\n")
        Display(str_content)
    except Exception as err:  # generic exception handling, if something goes wrong display the error #
        print("\nCongratulations. You broke the time continuum. Internal error\n")
        print(err)


def GetWebpage(str_url):
    # Get web page
    page_html = requests.get(str_url)
    # Parse with BeautifulSoup's html parser
    page_soup = soup(page_html.text, "html.parser")
    # Return result in soup format
    return page_soup


def ExtractPoem(page_soup):
    # Locate div tag, class - 'poem_body'
    found = page_soup.find("div", {"class": "poem_body"})
    # This strips all the leading white space from each paragraph
    poem = "\n".join(line.strip() for line in found.p.text.split("\n"))
    # Return parsed poem as string
    return poem


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
    str_content = import_file.read()                   # read file contents into variable
    # Close file
    # import_file.close   - not necessary to disabled
    return str_content


def Display(content):
    # Pretty simple, display contents of file. It's already formatted correctly
    print(content)


# Engage
if __name__ == '__main__':
    main()