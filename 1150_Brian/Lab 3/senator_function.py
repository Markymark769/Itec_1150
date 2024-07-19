"""
Mark Porraz
7/16/2024


"""
def main():
    state, age, us_citizen_years, current_state = get_user_input()
    age_check = check_age(age)
    citizenship_check = check_citizenship(us_citizen_years)
    residency_check = check_state_residency(current_state, state)
    output(age_check, citizenship_check, residency_check)

def get_user_input():
    state = input('What is the state you want to be a senator in?')
    age = int(input('What is your age?'))
    us_citizen_years = int(input('Have you been a citizen of the US for at least 9 years?'))
    current_state = input('What is the state that you currently live in?')
    return state, age, us_citizen_years, current_state

def check_age(age):
    if age >= 30:
        return 'You meet the requirement of being at least 30 years old.'
    else:
        return 'You do not meet the requirement of being at least 30 years old.'

def check_citizenship(us_citizen_years):
    if us_citizen_years >= 9:
        return 'You meet the requirements of living in the US for at least 9 years.'
    else:
        return 'Ineligible, you have not lived in the US for at least 9 years.'

def check_state_residency(current_state, state):
    if current_state == state:
        return 'You meet the requirement of living in the state you would like to represent.'
    else:
        return 'You do not meet the requirement of living in the state you would like to represent.'

def output(age_check, citizenship_check, residency_check):
    print(age_check)
    print(citizenship_check)
    print(residency_check)

main()

# def get_user_input():
#     state = input('What is the state you want to be a senator in?')
#     age = int(input('What is your age?'))
#     us_citizen_years = int(input('Have you been a citizen of the US for at least 9 years?'))
#     current_state = input('What is the state that you currently live in?')
#     return state, age, us_citizen_years, current_state
#
# def check_age(age):
#     if age >= 30:
#         return 'You meet the requirement of being at least 30 years old.'
#     else:
#         return 'You do not meet the requirement of being at least 30 years old.'
#
#
# def check_citizenship(us_citizen_years):
#     if us_citizen_years >= 9:
#         return 'You meet the requirements of living in the US for at least 9 years.'
#     else:
#         return 'Ineligible, you have not lived in the US for at least 9 years.'
#
#
# def check_state_residency(current_state, state):
#     if current_state == state:
#         return 'You meet the requirement of living in the state you would like to represent.'
#     else:
#         return 'You do not meet the requirement of living in the state you would like to represent.'
#
#
# def main():
#     state, age, us_citizen_years, current_state = get_user_input()
#     print(check_age(age))
#     print(check_citizenship(us_citizen_years))
#     print(check_state_residency(current_state, state))
#
#
# main()
