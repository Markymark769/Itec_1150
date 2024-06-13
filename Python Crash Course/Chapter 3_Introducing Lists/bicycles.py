bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
# Assessing Elements in a List
#####python can access an element in a list ranging from 0-whatever is needed
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())
#Index positions start at 0 and not 1. second item is 1.
#####not remembering where the index starts typically results in user error
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[1])
print(bicycles[3])
# python has special syntax. By using a negative it will return to the last item on the list.
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[-1])
# Using Individual Values from a List
bicycles = ['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)