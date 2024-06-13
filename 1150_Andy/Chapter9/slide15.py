
import os
my_file = open('my_file.txt', 'r')  	# r for read mode
my_line = my_file.readline()        	# read the first line
print('First line from file: ' + my_line)

# here it's used with a loop
while my_line != '':
    print(my_line, end='')  # end='' overides the default newline
    my_line = my_file.readline()   	# loop through a line at a time
my_file.close()  # close the file
