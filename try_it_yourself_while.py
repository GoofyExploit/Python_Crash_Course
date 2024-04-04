# # Pizza Toppings:

print("\nWelcome to our Pizza Shop.") 
active = True
while active:
    prompt = "\nEnter 'quit' to exit the Shop. "     
    prompt += "\nPlease, Enter the toppings you'd like on your Pizza: "
    prompt = input(prompt)
    if prompt != 'quit':
        print(f"\nAdding '{prompt.title()}' to your Pizza.")
    else:
        active = False
print(f"Thanks for entering our Shop.")

# # Movie Tickets:


active = True
while active:
    prompt = "\nWelcome to My Movie Theater!!!"
    prompt += "\nWhat is your Age? "
    age = int(input(prompt))
    if age < 3:
        print("Hurray, the ticket is free!")
    if 3 < age < 12:
        print("The ticket is $10.")
    if age > 12:
        print("The ticket is $15.")
    while True:
        cont = input("Do you wish to continue?(y or n) ")
        if cont.lower() == 'n':
            active = False
            break
        if cont.lower() == 'y':
            active = True
            break
        else:
            print("Invalid input, please enter y or n.")
        
print("Thank you, for using my Program. ")

# Infinity:

# while True:
#     print("hello")

# # Deli:

sandwich_orders = ['grilled sandwich','aloo sandwich','chicken sandwich','cheese sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(f"\nI made your {sandwich.title()}.")
print(f"\nSandwiches made:\n")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")

# # No Pastrami:

sandwich_orders = ['grilled sandwich','pastrami sandwich','aloo sandwich','pastrami sandwich','chicken sandwich','cheese sandwich','pastrami sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
while 'pastrami sandwich' in finished_sandwiches:
    finished_sandwiches.remove('pastrami sandwich')
print(f"\nDeli has run out of pastrami.")
for sandwich in finished_sandwiches:
    print(f"\nI made your {sandwich.title()}.")
print(f"\nSandwiches made:\n")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")

# # Dream Vacation:

dream_vacation = {}
polling_active = True

prompt = "\nIf you could visit one place in the world, where would you go? "
while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input(prompt)
    dream_vacation[name] = vacation
    repeat = input("Would you like anybody else to take this poll?(yes or no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, vacation in dream_vacation.items():
    print(f"{name.title()}, would like to go to {vacation.title()}.")