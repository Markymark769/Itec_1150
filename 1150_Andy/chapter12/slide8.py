"""
example) slide 8
"""

read_data = []  # create an array
read_file = open('romeo_juliet.txt', 'rb')  # 'r' mode also works – what's included???  WB stands for write binary
my_data = (read_file.readline())  # read a line
while my_data:  # loop while there is something to read
    read_data.append(my_data)  # append a file line to the array
    my_data = (read_file.readline())  # read the next line
print(len(read_data))  # how many lines in the array?
print(read_data)  # print the whole array
for line in read_data:  # loop through the array
    if read_data.index(line) < 100:  # let's just print 100 lines
        print(read_data.index(line), line)  # not all 4853!
    else:          # break after 100 lines - phew!
        break
