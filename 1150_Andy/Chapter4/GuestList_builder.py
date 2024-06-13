print('Welcome to the Guest List Builder')
guests = []

while True:
	new_guest = input('Type name & enter (hit enter twice to quit): ')
	if new_guest == '':
		break
	else:
		guests.append(new_guest)
print(guests) # compare results
print(*guests, sep = ", ")

for index in range(len(guests)):
	if index < len(guests) -1:
		print(f'Guest #{index + 1} is {guests[index]}, ', end = "")
	else:
		print(f'and Guest #{index + 1} is {guests[index]}.')

print('{:<30}{:>7}'.format('Guest Name','Ticket'))
for index in range(len(guests)):
	print('{:<30}{:>2}{:>5}'.format(guests[index],'#',index + 1001))
print('{:.<30}{:.>7}'.format('Total',len(guests)))
