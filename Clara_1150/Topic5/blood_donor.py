"""
Mark Porraz
2/21/2024
blood_donor.py
written by Clara James
To be a blood donor in the US, you need to be 17 or older, and weigh at least 110 lbs.
There are other requirements which we will ignore for this program.
"""

age = int(input('Please enter your age, in years: '))
weight = int(input('Please enter your weight, to the nearest pound: '))

# Decide if a person with this height and weight is eligible

if age >= 17 and weight >= 110:   # age must be greater or equal to 17  AND  weight must be greater or equal to 110
    print('You are eligible to donate blood, thank you so much for your interest in being a blood donor!')
else:
    # too young, or weight too low
    print('Thank you so much for your interest! Unfortunately, you are not eligible at this time. ')
    # check reasons for not being eligible, print specific message(s)
    if age < 17:
        print('You are too young, please consider donating blood when you are 17.')
    if weight < 110:
        print('Your weight is too low, for the health and safety of donors, they must weigh at least 110lbs.')


print('Thank you for your interest in blood donation. Please visit https://www.redcrossblood.org/ for more information.')