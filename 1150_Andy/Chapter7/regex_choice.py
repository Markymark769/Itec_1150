"""
Mark Porraz, 5/2/2023, regex_choice.py
Using regex, write 10 different expressions to find characters, words, phrases or patterns
– all searching in this same source text (my_song).
"""

import re  # import redex

my_song = ("""Sing me a song, you're a singer  
    Do me a wrong, you're a bringer of evil
    The Devil is never a maker
    The less that you give, you're a taker
    So, it's on and on and on
    It's Heaven and Hell
    Oh, well, yeah
    The lover of life's not a sinner
    The ending is just a beginnin'
    The closer you get to the meaning
    The sooner you'll know that you're dreaming """)  # Black Sabbath w/ Ronnie James Dio


patterns = [r'Heaven and Hell', r'\bs\w+er\b', r'Devil', r'\b\w*[aeiou]{2}\w*\b', r'[-,\']',
            r'The less that you give', r'\b[A-Z]\w*\b', r'\b[a-z]\w*\b', r'\b\w{5}\b', r'\b\w+ing\b']

pattern1 = r'Heaven and Hell'  # - pulls out instances of Heaven and Hell
result1 = re.findall(pattern1, my_song)
print(result1)

pattern2 = r'\bs\w+er\b'  # pulls out words that start with s and end in er.
result2 = re.findall(pattern2, my_song)
print(result2)

pattern3 = r'Devil'  # pulls out all instances of the word Devil
result3 = re.findall(pattern3, my_song)
print(result3)

pattern4 = r'\b\w*[aeiou]{2}\w*\b'  # pulls out vowels
result4 = re.findall(pattern4, my_song)
print(result4)

pattern5 = r'[-,\']'  # pulls out all instances of a hyphen or a single quote
result5 = re.findall(pattern5, my_song)
print(result5)

pattern6 = r'\bs\w+er\b'  # pulls out words that are lowercase
result6 = re.findall(pattern6, my_song)
print(result6)

pattern7 = r'The less that you give'  # pulls out phrases the less you give
result7 = re.findall(pattern7, my_song)
print(result7)

pattern8 = r'\b[A-Z]\w*\b'  # - pulls out words that start with a capital
result8 = re.findall(pattern8, my_song)
print(result8)

pattern9 = r'\b\w{5}\b'  # - pulls out all instances of 5 character
result9 = re.findall(pattern9, my_song)
print(result9)

pattern10 = r'\b\w+ing\b'  # - pulls out all instances of ing
result10 = re.findall(pattern10, my_song)
print(result10)


# unused code
# for pattern in patterns:
#     results = re.search(pattern, my_song)  # find all the results of the pattern from my_song
#     print(results.group())  # print them



