
import os

my_file = open('my_file.txt', 'r')  # r for read mode
my_data = my_file.readlines()  # read the entire file into a list
print(my_data)
my_file.close()  # close the file
