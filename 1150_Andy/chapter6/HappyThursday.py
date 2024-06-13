"""
Happy Wednesday
"""

stuff = input('Type in a sentence with 3 spaces at..')
print('1 ' + stuff + '!')
print('2 ' + stuff.strip() + '!')  # takes from both sides
print('3 ' + stuff.rstrip() + '!')  # takes from the left side
print('4 ' + stuff.lstrip() + '!')  # takes from the right side
print()

sentence = ' This is a sentence.'
word_list = sentence.split()
print(word_list)
print()

sentences = 'This is a sentence. This is one too.'
sentence_list1 = sentences.split('.')  # has empty item
print(sentence_list1)
sentence_list1.pop()  # good, but 2nd item has a leading space
#  what does pop do? get rid of an empty item, pops ot the last item in the list
sentence_list2 = []
for index in range(len(sentence_list1)):
    sentence_list2.append(sentence_list1[index].strip())
print(sentence_list2)  # all goof, but a pain

