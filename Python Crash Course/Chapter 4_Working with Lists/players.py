# Working with Part of a List
## Slicing a List
##### slice- specifying the first and last elements you want to work with. 
##### 
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
##### the code prints out the first three players

players = ['charles','martina','michael','florence','eli']
print(players[0:4])
##### the code prints out the first four players
##### starts with 'martina' and ends with 'florence'

players = ['charles','martina','michael','florence','eli']
print(players[:4])
##### the code uses a different notation
##### prints out the first four players becuase you failed to omit the first index

players = ['charles','martina','michael','florence','eli']
print(players[2:])
##### prints out the first three players becuase you failed to omit the second index

players = ['charles','martina','michael','florence','eli']
print(players[-3:])
##### prints the last three players


players = ['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
##### instead of looping through the entire list of players, it loops through
##### only the first three names