"""

Mark P
1/31/2024
Dollar
professor clara


"""




# boolian staments mean ture or false
# # true/False and 'if' statements
#
# # up to this point, everythiing we type in as code gets run like so:
# print("I took the red pill.")
# print("I took the blue pill.")
#
# # We often want to make decisions to do one thing or another
# # we do this based on circumstances or conditions. In programming,
# # we express these circumstances or conditions using ture or false values.
#
# # check the true branch
#
# # if True:
# #     print(" This is the branch when true")
# # else:
# #     print("This is the branch when False.")
# #
# # # it is highlighted when it is false. the IDE does parsing to know that this will not ever be true
# #
# # if False:
# #     print("This is the branch when True")
# # else:
# #     print("This is when the branch is False.")
#
# # But usually, you have true/false stored in value:
# i_went_into_the_matrix = False
# if i_went_into_the_matrix:
#     print("I took the red pill.")
# else:
#     print("I took the blue pill.")
#
# # we have to check for conditions
# if 0 < 1:
#     print("0 is less than 1")  # A --- congrats you qualify
# else:
#     print("0 is NOT less than 1.") # B ----sorry you do not qualify
#
# # if/elif/else
# # myNumber = 4
# # if myNumber < 3:
# #     print("less than 3")
# # elif myNumber < 5:
# #     print("greater than or equal to 3 or less than 5")
# #
# # else:
# #     print("greater than 3")
#
#
# myNumber = 6
# if myNumber < 3:
#     print("less than 3.")
# elif myNumber < 5:
#     print("greater than or equal to 3 or less than 5.")
# elif myNumber < 7:
#     print(" greater than or equal to 5 or less than 7.")
# else:
#     print("greater than 3.")
#
# #Class question
# # Question 1:
# # What to I replace ??? with if I want to print 'pass!' when:
# #   coin flip is "heads" AND...
# #   die roll is greater than 3
# #
# # Question 2:
# # Change variables so that 'fail!' prints
# #
# # Question 3:
# # Change so that it prints 'pass!' if
# #   coin flip is "heads" AND...
# #   die roll is greater than 3
# coin_flip = "heads"
# die_roll = 5
# if (dice_roll > 3) and (coin_flip == 'heads'):
#     print("pass!")
# else:
#     print("fail!")
#
# evar = 'e'
# bvar = 2
# if (avar == 'a') and (bvar > 1):
#     print('true')
# else:
#     print('false')

# name = 'Carol'
# age = 3000
#
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 100:
#     print('You are not Alice, grannie.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')

print('Hello')
name = input('what is your name')  # this a string, only prints string of letters
age = int(input('how old are:'))  # we have to be specific and tell pycharm we need integers not strings
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
