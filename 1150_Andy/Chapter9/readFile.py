import os
my_file = open('my_file.txt', 'r')  # r is for read mode
my_data = my_file.read()  # read the entire file into one string
print(my_data)
my_file.close()  # close the file 