# # Personal Message:

name = 'Lucky'
message = f"Hello {name}, would you like to learn Python today?"
print(message)

# # Name Cases: 

name = 'lucky'
print(name.title())
print(name.upper())
print(name.lower())

# # Famous Quote:

author = 'Bruce Lee'
quote = '"Be like water my friend."'
message = f"{author} once said, {quote}"
print(message)

# # Stripping Names:

name = '\tLucky\t'
print(name)
new_name1 = name.lstrip()
new_name2 = name.rstrip()
new_name3 = name.strip()
print(new_name1)
print(new_name2)
print(new_name3)


# # File Extensions:

filename = 'python-notes.txt'
print(filename.removesuffix('.txt'))