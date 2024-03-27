# # Seeing the world:

places = ['new york','australia','vrindavan','mathura','ayodhya']
print(places)
sorted = sorted(places)
print(sorted)
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort()
print(places)

# # Dinner Guests:

invite = ['amit','prashant','kanav','anvit','parth','dhruv']
length = len(invite)
print(length)

# # Every function:

cities = ['new york','tokyo','sydney']
cities.append('canda')
print(cities)
cities.insert(0,'amsterdam')
print(cities)
del cities[0]
print(cities)
cities.remove('sydney')
print(cities)
popped_city = cities.pop()
print(popped_city)
print(cities)

# # Reverse without reverse method:

name = ['amit','lucky','prashant','kanav']
print(name)
popped_name1 = name.pop()
name.insert(0,popped_name1)
popped_name2 = name.pop()
name.insert(1,popped_name2)
popped_name3 = name.pop()
name.insert(2,popped_name3)
popped_name4 = name.pop()
name.insert(3,popped_name4)
print(name)