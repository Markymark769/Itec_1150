"""
Mark Porraz
9/26/2023
Functions
Chapter 3
"""
# WHat is a function?
# a function in computer programming is a recipe for things to do
# a way to do repetitive tasks

# see pptx
# used for function vocabulary
# example 1
def biggerThanThree(diceRoll):
    if diceRoll < 1 or diceRoll > 6:
        print("Not a number on a die.")
    elif (diceRoll >3):
        print("It\s bigger than 3!")
    else:
        print("It is 3 or smaller")
biggerThanThree(4)

# example 3
# a function can do things but it can retrtn things that you want to assign to an actual variable

def jutPrintNotReturn(name):
    print(f"My name is {name}")

#This does print
jutPrintNotReturn('Mark')
retValue = jutPrintNotReturn('Mark')
print(f'The retValue is: {retValue}')

# However, you can retunr VAlues
def returnNoPrint(name):
    return f'My name is {name}.'

# Notice that it doesnt print by default. you need to make it print
returnNoPrint('Mark')

# Now print
strToPrint = returnNoPrint("Matt")
print(f"returnNoPrint() returned string: [{retValue}]")

# you can make it return multiple values, and capture them like this:
# some you can print and some you ccan rertuen values
# note) you can see the values that you hvae stored on the side in the terminal

def returnMultiValue(a,b,c):
    return f"first is {a}", f"second is {b}", f"Third is {c}"

fst, snd, thrd = returnMultiValue("Dewey","Cheatham","Howe")
print(f"snd is string: [{snd}]")

# what is the intent of a function? - it is a recipe to connect code
# use functions becuase you dont want to re-write things over agian
# while pos_int.isnumeric() is False or int(pos_int) == 0:
    # if i didn't get a number or i got a zero, I am going to be asking until i get a correct answer

def get_pos_int():
    pos_int = input('Please enter a whole number')
    while pos_int.isnumeric() is False or int(pos_int) == 0:
        pos_int = input('Enter a whole number greater than 0')
    pos_int = int(pos_int)
    return pos_int

myWidth = get_pos_int()
myHeight = get_pos_int()

print(f"Area is: {myWidth * myHeight}.")

# example 6
def main():
    number1 = int(input('Please type a number: '))
    cube(number1)
    number2 = int(input('Please type another number: '))
    cube(number2)

def cube(x):
    number_cubed = x**3
    print(f'The cube {x} is {number_cubed}')
main() # main fucntion is finally called
# MIPO
# MIPO stands for Main, Inputs, Processing, Outputs
# it will help you capsulate



