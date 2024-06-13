# the main() function should always be at the top
def main():
    Num1 = 6
    MyString = inputs()
    processing(MyString)
    outputs(Num1)
    print("That's all follks!")


# gather the input data
def inputs():
    Num1 = 'hello'
    print(1, Num1)
    return Num1  # to line 4 the value 'hello'


def processing(bNum):
    print(1.5)
    outputs(bNum)
    # go to line 6


def outputs(aNum):
    print(2, aNum)                   
    # go to line 16 or 6


main()  # call main()