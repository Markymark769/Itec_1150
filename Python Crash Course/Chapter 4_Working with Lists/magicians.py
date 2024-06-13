# Using the for loop
# avoids being repetitive and dont have to change code each time the length is changed.
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
# A Closer Look at Looping
#
#magicians = ['alice','david','carolina']
##### 
#for magician in magicians:
##### Tells python to retrieve the first value from the list, which is 'alice'
##### takes the first value and associates it with the variable, magician
#    print(magician)
##### prints the current value of magician, which is still 'alice'
##### Python will cycle through the code until it reaches the end of the list
##### which is 'Carolina', because no more values are in the list. 

#Doing More Work Within a for Loop
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
##### adding more sentences to the code
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
#####          common errors are 
##### 1-forgetting to indent
##### 2-forgetting to indent additional lines
##### 3-indenting unnecessarily 
##### 4-indenting unnecessarily after the loop
##### 5-forgetting the colon
