# # Person:

person = {
    'first_name':'lucky',
    'last_name':'grover',
    'age':19,
    'city':'rohtak',
}
print(person)

# # Favorite Numbers:

fav_num = {
    'edward':25,
    'alphonse':45,
    'gin':20,
    'ichigo':7,
    'rukia':69,
}
print(fav_num)

# # Glossary:

glossary = {
    'python':"it's a very effective programming language.",
    'loop':'it helps you repeat a certain task.',
    'function':"it's a piece of code that can be used again and again.",
    'conditional statements':'these are the statements that helps you compare things.',
    'print':'this is a function in python that prints a certain text you want.'
}
dictionary = print(f"\nGlossary:\n1. Python: {glossary['python'].capitalize()}\n2. Loop: {glossary['loop'].capitalize()}\n3. Function: {glossary['function'].capitalize()}\n4. Conditional Statements: {glossary['conditional statements'].capitalize()}\n4. Print: {glossary['print'].capitalize()}\n")

print(f"{dictionary}")

# differnt approach using for loop:

print("\nGlossary:\n")
for language, description in glossary.items():
    print(f"{language.capitalize()}: {description.capitalize()}\n")