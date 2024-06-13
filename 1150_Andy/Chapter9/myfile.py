# import os
# my_file = open('my_file.txt', 'w')  # w is for write mode
# my_file.write('Hello Earth!\n')
# my_file.write('Hello Mars!\n')
# my_file.close()
# print('Done!')

import os
my_file = open('my_file.txt', 'a')  # 'a' is for append mode
my_file.write('Hello Venus!\n')
my_file.write('Hello Jupiter!\n')
my_file.close()
print('Done again!')
