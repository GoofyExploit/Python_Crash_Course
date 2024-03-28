# # Alien Colors 1:

alien_color = 'green'
if alien_color == 'green':
    print('Player just earned 5 points.')
if alien_color == 'red':
    print()

# # Alien Colors 2:

alien_color = 'green'
if alien_color == 'green':
    print('Player just earned 5 points for shooting the alien.')
else:
    print('Player just earned 10 points.')

alien_color = 'red'
if alien_color == 'green':
    print('Player just earned 5 points for shooting the alien.')
else:
    print('Player just earned 10 points.')

# # Alien Colors 3:

alien_color = 'green'
if alien_color == 'green':
    print('Player earned 5 points.')
elif alien_color == 'red':
    print('Player eanred 15 points.')
elif alien_color == 'yellow':
    print('Player earned 10 points.')

alien_color = 'yellow'
if alien_color == 'green':
    print('Player earned 5 points.')
elif alien_color == 'red':
    print('Player eanred 15 points.')
elif alien_color == 'yellow':
    print('Player earned 10 points.')

alien_color = 'red'
if alien_color == 'green':
    print('Player earned 5 points.')
elif alien_color == 'red':
    print('Player eanred 15 points.')
elif alien_color == 'yellow':
    print('Player earned 10 points.')

# # Stage of Life:

age = 12
if age < 2:
    stage = 'a baby'
elif age >= 2 and age < 4:
    stage = 'a toddler'
elif age >= 4 and age < 13:
    stage = 'a kid'
elif age >= 13 and age < 20:
    stage = 'a teenager'
elif age >= 20 and age < 65:
    stage = 'an adult'
elif age >= 65:
    stage = 'an elder'
print(f"Person is {stage}.")

# # Favorite Fruit:

favorite_fruits = ['mango','apple','banana']
for fruit in favorite_fruits:
    if fruit in favorite_fruits:
        print(f"You really like {fruit}!")  