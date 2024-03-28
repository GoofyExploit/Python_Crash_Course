# # Slices:

cities = ['new york','amsterdam','dubai','shanghai','berlin','tokyo','london']
print('The first three cities of my list are:')
for city in cities[:3]:
    print(city)

print('\nThe three cities from the middle of my list are:')
for city in cities[2:5]:
    print(city)

print('\nThe last three cities from my list are: ')
for city in cities[-3:]:
    print(city)

# # My Pizzas, Your Pizzas:
    
my_pizzas = ['chicago pizza','new york pizza','greek pizza']
my_pizzas.append('italian pizza')
friend_pizzas = my_pizzas[:]
friend_pizzas.append('brick oven pizza')
print('my favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)
print("\nmy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)