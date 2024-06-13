# \t to tab in the front -------------------------Adding Whitespace-----
print("python")
print("\tPython")
## to add a newline in a string, use the character \n
print("Languages:\nPython\nC\nJavaScript")
###combine tabs and newlines in a single string. use the chatacter \n\t, to move a new line and start with the next tab.
print("Languages\n\tPython\n\tC\n\tJavaScript")
# the following below strips whitespace ----------Stripping whitespace-----
##rstip() menthod
### need to look up tutorial
favorite_language = 'python !'
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)
favorite_language = 'python '
print(favorite_language.rstrip())
favorite_language = ' python!'
print(favorite_language)
#### strips left --> .lstrip() method
print(favorite_language.lstrip())
##### strips from both sides --> .strip() method
print(favorite_language.strip())
print(favorite_language)