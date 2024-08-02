"""
Brian Huilman

"""

# https://www.lyrics.com/lyric/683080/New+Order/Blue+Monday
lyrics = """How does it feel
To treat me like you do?
When you've laid your hands upon me
And told me who you are?
Thought I was mistaken
I thought I heard your words
Tell me, how do I feel?
Tell me now, how do I feel?

Those who came before me
Lived through their vocations
From the past until completion
They'll turn away no more
And I still find it so hard
To say what I need to say
But I'm quite sure that you'll tell me
Just how I should feel today

I see a ship in the harbor
I can and shall obey
But if it wasn't for your misfortune
I'd be a heavenly person today
And I thought I was mistaken
And I thought I heard you speak
Tell me, how do I feel?
Tell me now, how should I feel?

Now I stand here waiting

I thought I told you to leave me
While I walked down to the beach
Tell me, how does it feel
When your heart grows cold?"""
lyrics = lyrics.lower()
punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ':', ';', '"', ',', '<', '.', '>', '/', '?', '`', '~', '\'']
for mark in punctuation:
    lyrics = lyrics.replace(mark, '')
words = lyrics.split()
print(f'There are {len(words)} words in the song.')
lines = lyrics.split('\n')
print(f'There are {len(lines)} lines in the song.')

# for printing
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
print(f'The {len(word_count)} unique words in the song are:')
for word in word_count:
    print(f'{word} ', end='')
print('\n')
print(f'{"Word:":<12}{"Frequency:":<10}\n')
for word, count in word_count.items():
    print(f'{word:<12}{count:<10}')


# print the frequency sorted dictionary
print('\n')
print(f'{"Word:":<12}{"Frequency:":<10}\n')
# https://docs.python.org/3/howto/sorting.html#sortinghowto
from operator import itemgetter
sorted_word_count = sorted(word_count.items(), key=itemgetter(1), reverse=True)
# [('i', 20), ('me', 11), ... ('grows', 1), ('cold', 1)]
for item in sorted_word_count:
    print(f'{item[0]:<12}{item[1]:<10}')