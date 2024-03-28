players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-2:])

print('Here are the first three players of our team:')
for player in players[:3]:
    print(player)

# # Copying a list:

my_foods = ['pizza','falafel','carrot cake']
my_foods.append('cannoli')
friend_foods = my_foods[:]
friend_foods.append('icecream')
print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
