"""Mark Porraz, 2/5/2023, This program will categorize
by type and grand total. Uses Boolean logic block to display
either < $10, > $10, or = $10.
"""
# asks for user input
q = input('How many quarters do you have? Enter a whole number please: ')
d = input('How many dimes do you have? Enter a whole number please: ')
n = input('How many nickles do you have? Enter a whole number please: ')
p = input('How many pennies do you have? Enter a whole number please: ')

# calculates the total of individual coins
q_total = int(q) * 0.25
d_total = int(d) * 0.10
n_total = int(n) * 0.05
p_total = int(p) * 0.01
coins = int(q) + int(d) + int(n) + int(p)  # keep having an issue here to find total numbers of coins
# grand total formula
grand_total = q_total + d_total + n_total + p_total

# places the user input in conditional statement
# makes sure input is a whole number
if (int(q) is False) or (int(q) < 0):
    print('Sorry, please put in a whole number.')
if (int(d) is False) or (int(d) < 0):
    print('Sorry, please put in a whole number.')
if (int(n) is False) or (int(n) < 0):
    print('Sorry, please put in a whole number.')
if (int(p) is False) or (int(p) < 0):
    print('Sorry, please put in a whole number.')


# Boolean print statements
else:
    if grand_total < 10.00:
        print(f'Keep saving! You have less than $10.00.')

    elif grand_total == 10.00:
        print(f'Keep saving! You have exactly $10.00')

    elif grand_total > 10.00:
        print(f'Keep saving! You have more than $10.00.')

# print columns
# 4 columns total
print('Total value of your coins.')
print('{:<14}{:<14}{:<4}{:<12}'.format('Coin Type', 'Number', '', 'Value'))
print('{:<14}{:<14}{:<4}{:<12,.2f}'.format('Quarters', q, '$', q_total))
print('{:<14}{:<14}{:<4}{:<12,.2f}'.format('Dimes', d, '$', d_total))
print('{:<14}{:<14}{:<4}{:<12,.2f}'.format('Nickles', n, '$', n_total))
print('{:<14}{:<14}{:<4}{:<12,.2f}'.format('Pennies', p, '$', p_total))
print('{:<14}{:<14}{:<4}{:<12,.2f}'.format('Total', coins, '$', grand_total))
print("That's all folks.")
