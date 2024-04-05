# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
# greet_user()

# def greet_user(username):
#     """Display a simple greeting"""
#     print(f"Hello, {username.title()}")
# greet_user('jesse')

# # Positional Arguments:

# def describe_pet(animal_type,pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster','harry')
# describe_pet('dog','willie')

# # Keyword Arguments:

# def describe_pet(animal_type,pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster',pet_name='harry')

# # Default Values:

# def describe_pet(pet_name,animal_type='dog'):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='willie',animal_type='hamster')

# Return Values:

# def get_formatted_name(first_name,last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi','hendrix')
# print(musician)

# # Making an argument optional:

# def get_formatted_name(first_name,last_name,middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi','hendrix')
# print(musician)
# musician = get_formatted_name('john','hooker','lee')
# print(musician)

# # Returning a Dictionary:

# def build_person(first_name,last_name):
#     """Return a dictionary of information about a person"""
#     person = {'first':first_name,'last':last_name}
#     return person
# musician = build_person('jimi','hendrix')
# print(musician)

# def build_person(first_name,last_name,age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi','hendrix',age=27)
# print(musician)

# # using a function with a while loop:

# def get_formatted_name(first_name,last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello, {formatted_name}")

# # Passing a List:

# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)
# usernames = ['hannah','try','margot']
# greet_users(usernames)

# # Modifying a list in function:

# def print_models(unprinted_designs,completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each desgin to completed_models after printing.
#     """

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []

# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)

# # Preventing a Function from modifying a List:

# def print_models(unprinted_designs,completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each desgin to completed_models after printing.
#     """

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []

# print_models(unprinted_designs[:],completed_models)
# show_completed_models(completed_models)