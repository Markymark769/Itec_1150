"""
Mark Porraz
2/6/2024
January.py

Question 1: For loops - January Calendar (5 points)

Write a program that uses a loop to print the date for every day in January.
So, your program's output will look like this. Make sure the first date is "January 1"
 and the last date is "January 31". You'll only need one print statement - don't write 31 print statements!

"""



print('The dates in January are:')
for i in range(31):
    print('January (' + str(i+1) + ')')  # function (' + str(i) + ') added

name = 'Enter your name'