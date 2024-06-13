"""
Mark Porraz
2/29/2024
Lists example
"""
# # example 1
print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are: ')
print(catName1+''+catName2 + '' + catName3 + '' + catName4 + '' + catName5 + '' + catName6)

# updated example 1 using a list
catNames = []

while True:
    print('Enter the name of cat' + str(len(catNames) + 1) + '(Or enter nothing to stop):' )
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('' +name)  # the empty string is just used for putting an empty space in the program
print('So many cats!')

# (note)
# a While loop can be used for using something when you don't
# know how many times your program is going to loop over.
#
# a For loop is used for something when you know the definite number
# of things you will get.

# streets = ['Lake', 'Hennepin', 'Lyndale']
# print(streets)
# print(streets[1])
# print()
#
# villains = ['Voldemort', 'Darth Vader', 'Sauron']  # string data
# quiz_scores = [10, 9, 10, 8]  # int data
# rainfall_amts = [0.8, 1.3, 1.1, 2.1, 2.6, 0.2, 0.6]  # float data
# mixed_items = ['Hello', 100, 5.55]  # varying data types
# list_of_lists = [[1,2,3], [4,5,6]]  # nested list data
#
# first_villain = villains[0]
# print(first_villain)
# second_quiz_score = quiz_scores[1]
# print(second_quiz_score)
# fifth_rainfall = rainfall_amts[4]
# print(fifth_rainfall)
#
# villains[0] = 'Catwoman'  # this overwrites any value at this list position
# print(villains)
# quiz_scores[1] = 10
# print(quiz_scores)
# rainfall_amts[4] = 1.2
# print(rainfall_amts)
#
# streets.sort()
# print(streets)
#
# rainfall_amts = [0.8, 1.3, 1.1, 2.1, 2.6, 0.2, 0.6]
# rainfall_amts.sort()
# print(rainfall_amts)
# total_rain = sum(rainfall_amts)
# avg_rain = round(sum(rainfall_amts) / len(rainfall_amts), 2)
# min_rain = min(rainfall_amts)
# max_rain = max(rainfall_amts)
# print(f'Weekly rain facts: \nMin {min_rain}\tMax {max_rain}\tAvg {avg_rain}\tTotal {total_rain}')
#
# # Best method – works as expected, even if list items are repeated
# list_of_colleges = ['MCTC', 'Metro State', 'SPC', 'MCTC']
# for index in range(len(list_of_colleges)):
# 	print(f'College #{index+1}')
# 	print(f'Name: {list_of_colleges[index]}')
# print('\n')
# # For the curious… Compare to this method & NOTE what happens to 4th item…')
# for college in list_of_colleges:
# 	print(f'College #{list_of_colleges.index(college)+1}')
# 	print(f'Name: {college}')
#
# # math operations and formatting can be applied to each list item, in a loop
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index in range(len(numbers)):
# 	squared = numbers[index] ** 2
# 	print(f'{numbers[index] :>2d} squared is {squared :>3d}')
#
# villains = []  # initialize emply list
# villains.append('Catwoman')
# villains.append('Darth Vader')
# villains.append('Sauron')
# villains.append('Lex Luthor')
# villains.append('Magneto')
# print(villains)


