"""
Mark Porraz, 4/19/2023,
Slides 15 + 16 + 17.
"""
# # slide 15
# sentence = 'This is a sentence.'
# word_list = sentence.split()
# print(word_list)
#
# # slide 16
# # example 1
# sentences = 'This is a sentence. This is too.'
# sentence_list1 = sentences.split('.') ## has empty item
# sentence_list1.pop()  ## gets rid of empty item
# print(sentence_list1) ## good, but 2nd item has leading space
# sentence_list2 = []
# for index in range(len(sentence_list1)):
#     sentence_list2.append(sentence_list1[index].strip())
# print(sentence_list2)  ## all good, but a pain!

# example 2
# sentences = 'This is a sentence. This is too.'
# sentence_list2 = []
# for sentence in sentences.split('.'):
#     if sentence:  # leaves out empty item
#         sentence_list2.append(sentence.strip())
# print(sentence_list2)


# slide 17

# sentence = 'This is a word list.'
# word_list = sentence.split()
# print(word_list)
# print('Here is your word list fixed & printed nicely')
# new_word_list = []
# for index in range(len(word_list)):
# 	if index < len(word_list) - 1:
# 		new_word_list.append(word_list[index].lower().strip())
# 		print(f'Word {index +1}: {new_word_list[index]}')
# 	else:
# 		new_word_list.append(word_list[index].lower().strip().replace(".", ''))
# 		print(f'Word {index + 1}: {new_word_list[index]}')
# print(new_word_list)

# phone = 'computer'
# print(phone[5])  # prints  the letter i
# print(len(phone))  # prints 7
# for i in 'Android':
# 	print(i.upper(), end = " ") # try w/ and without end = " "

#
# phone = 'Android'
# length = len(phone)  # returns 7
# #last_letter = phone[length]  # causes index error
# #print(last_letter)
#
# # shorthand to access the last letter in a string variable
# print(phone[len(phone)-1])

sentences = 'This is a sentence. This is too.'
sentence_list1 = sentences.split('.') # has empty item
sentence_list1.pop()  # gets rid of empty item
print(sentence_list1) # good, but 2nd item has leading space
sentence_list2 = []
for index in range(len(sentence_list1)):
    sentence_list2.append(sentence_list1[index].strip())
print(sentence_list2)  # all good, but a pain!

spelling_mistakes = 'I am going too school too learn programming.'
correct = spelling_mistakes.replace('too', 'to')
print(correct)
sentence = 'My ca=t pres==ses= the equals= key= when I ty=pe.'
new_sentence = sentence.replace('=', '')
print(new_sentence)

stuff = input('Type in a sentence with 3 spaces at the beginning and at the end!')
print('1 '+stuff+'!')
print('2 '+stuff.strip()+'!')
print('3 '+stuff.rstrip()+'!')
print('4 '+stuff.lstrip()+'!')


