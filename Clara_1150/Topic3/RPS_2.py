"""
Mark Porraz
1/24/2024
Rock Paper Scissors.py
"""
import random  # in python there are things that are just built in and just knows what to do
# random can generate random numbers
#  in python we have things called lists

possible_choices = ['rock', 'paper', 'scissors']  # square brackets = make a list of strings

computer_choice = random.choice(possible_choices)

print(computer_choice)
