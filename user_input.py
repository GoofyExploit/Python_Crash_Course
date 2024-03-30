message = input("Tell me something, and i will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you share your name, we can personlize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print(f"\nYou are tall enough to ride!")
else:
    print(f"\nYou'll be able to ride when you're little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"The Number {number} is even.")
else:
    print(f"The number {number} is odd.")