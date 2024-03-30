# # Rental car:

car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car.title()}.")

# # Restaurant Seating:

people = input("How many people are in your dinner group? ") 
people = int(people)
if people > 8:
    print(f"You'll have to wait for a table.")
else:
    print(f"Your table is ready.")

# # Multiples of Ten:

number  = input("Please enter a number: ")
number = int(number)
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")