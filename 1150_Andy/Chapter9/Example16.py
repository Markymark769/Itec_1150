
import os
if os.path.isfile('party_invites.txt') is False:  # turn off-line if you DON'T want to keep file between runs
    invite_file = open('party_invites.txt', 'w')  # 'w' for write
    invite_file.write('Hostess - Betty Boop\n') # initialize a txt file
    invite_file.close()

# original input is a string, with commas separating each entry
user_input = input('Enter guest names, separating each one with a comma. ')
user_input_list = user_input.split(',')  # change to a list
user_input_fixed = ''  # a new string to hold the fixed items, so they can be written to the file
invite_file = open('party_invites.txt', 'a')  # 'a' for append mode

for i in range(len(user_input_list)):
    guest_fixed = user_input_list[i].strip()
    user_input_fixed = 'Guest ' + str(i + 1) + ' - ' + guest_fixed + '\n'
    invite_file.write(user_input_fixed)
invite_file.close()
