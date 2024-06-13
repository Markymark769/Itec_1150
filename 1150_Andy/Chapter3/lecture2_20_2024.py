# def foo(name_parameter):
#     print(f"I am {name_parameter}.")
#
# foo(name_parameter="Groot")
#
#
# def foo(name_parameter):
#     if name_parameter == "Groot":
#         print(f"I am {name_parameter}.")
#     else:
#         print(f"Hello, my name is {name_parameter}.  Nice to meet you.")
#
# foo("Groot")
# foo("Rocket")
#
# def foo(first_name, second_name):  # we have two parameters
#     print(f"{first_name}, meet {second_name}.")
#
# foo("Groot", "Rocket")

# def foo(first_name, second_name):
#     print(f"{first_name}, meet {second_name}.")
#
# foo("Groot")
#
# def foo():
#     return 11 # the fucntion retunrs a value which you can see as a variable.
#
# # What happens here?
# the_value = foo()
# print(f"The values is: {the_value}.")

# def foo():
#     return 11, 888
#
# first_number, second_number = foo()
# print(f"First number: {first_number}, second number: {second_number}.")
#
# def foo(first_number, second_number):
# #     return first_number > second_number
#
# the_result = foo(32, 54)
# print(f"The result: {the_result}.")
#
# the_result = foo(54, 32)
# print(f"The result: {the_result}.")

# What does this do?
# def foo(number_p1):
#     return 3 * number_p1
#
# def bar(number_p2):
#     return foo(number_p2) + 1
#
# the_result = bar(5)
# print(f"The result: {the_result}.")
# # Does this work, with the same function parameter name?
# def foo(number_parameter):
#     return 3 * number_parameter
#
# def bar(number_parameter):
#     return foo(number_parameter) + 1
#
# the_result = foo(7)
# print(f"The result: {the_result}.")