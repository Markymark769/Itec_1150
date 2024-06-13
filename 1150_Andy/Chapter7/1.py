import re

my_song = """Sing me a song, you're a singer  
        Do me a wrong, you're a bringer of evil
        The Devil is never a maker
        The less that you give, you're a taker
        So, it's on and on and on
        It's Heaven and Hell
        Oh, well, yeah
        The lover of life's not a sinner
        The ending is just a beginnin'
        The closer you get to the meaning
        The sooner you'll know that you're dreaming """  # Black Sabbath w/ Ronnie James Dio

patterns = [
    r'Heaven and Hell',
    r'\bs\w+er\b',
    r'Devil',
    r'\b\w*[aeiou]{2}\w*\b',
    r'[-,\']'
]

for pattern in patterns:
    results = re.findall(pattern, my_song)
    print(results)
