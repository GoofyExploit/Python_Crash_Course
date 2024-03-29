# # Make an empty list for storing aliens.
aliens = []
# Make 30 green green aliens.
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print('...')
# show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# # Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print('...')

# # A list in a Dictionary:

# Store information about a pizza being ordered.
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

favortite_languages = {
    'jen': ['python','rust'],
    'sarah': 'c',
    'edward': ['rust','go'],
    'phil': ['python','haskell'],
}
for name, languages in favortite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for langauge in languages:
            print(f"\t{langauge.title()}")

# # A dictionary in a Dictionary:

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")