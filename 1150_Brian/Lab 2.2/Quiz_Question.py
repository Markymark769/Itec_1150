"""
Mark Porraz
Quiz_question.py

update this code to use a while loop

code to modify:
print("Quiz program!")
answer = input("What is the capital of Wisconsin? ")   # It's Madison
correct_answer = "Madison"
if answer == correct_answer:
    print("Correct!")
else:
    print(f"Sorry, the answer is {correct_answer}.")

"""

print("Quiz program!")

while True:
    answer = input("What is the capital of Wisconsin? ")   # It's Madison
    correct_answer = "Madison"
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Sorry, the answer is {correct_answer}.")
