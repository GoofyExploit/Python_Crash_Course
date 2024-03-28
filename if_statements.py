cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = ['mushrooms','onions','[pineapple]']
if 'mushrooms' in requested_toppings:
    print(f"{requested_toppings[0].title()} are requested")
elif 'pepperoni' not in requested_toppings:
    print('pepperoni is not requested')

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response as you wish.")

age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote?')
else:
    print("Sorry, you are to young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 3
if age < 4:
    price = 0
elif age >= 4 and age <= 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}")

requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinished making your pizza!')