"""
Mark Porraz
Chapter 9: Reading and Writing Files
Lecutre for Matt's class
"""

# file input and output is very important
# what is a file within a file system? a file is a container for other things, Files or more folders

# root directory, in windows it will be C: and in Mac it will be \:
# the file contains the information that uou want to process.

import os

# print('Current working directory - compare yours to the example.')
# print('Results of running: os getcwd()')
# proj_dir

os.chdir('D:\PycharmProjects')
print(f'current directory: {os.getcwd()}')

# know the difference between writing and append
# write will write over the file, erasing the contents of what was in there before
# appending will add to the file without erasing it
# how would you read a file? my_data = myfile.read()
# my_file = open('my_file','r')
# my_data = my_file.read()
# print(my_data)
# my_file.close()

# the hard thing with path seperators is that
# macs uses the conventional path seporator = / forward slash
# windows use the other convention path seporator = \ backslash
# windows - the \ backslash is also the escape character or a path seperator
# there are librarys


# pathlib
# the backslash is doubled up, escaping the escape
 from pathlib import Path
 os.getcwd()
 Path.cwd()
 print(Path.cwd())
 print(Path.cwd() / 'my_file.txt')


