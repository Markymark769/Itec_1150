def myAdd():
    print(f"{x + y}")

def randoDanger():
    global x
    x = 100

# Perfectly normal...
x = 2
y = 3

#;; As you'd expect
myAdd()

print("And then a wild rando comes along...")
randoDanger()
myAdd()

def myAddSafe(x, y):
    print(f"{x + y}")

myAddSafe(2, 3)