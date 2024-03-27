message = "Hello Python Interpreter!"
print(message)

# # Simple Message Exercise

message = "my name is lucky"
print(message)

# # Strings:

name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# # whitespaces:

print("\tLucky")
print("Languages:\n1.Python\n2.Java\n3.Ruby")

# # Stripping Whitespaces:

fav_lang = 'Python '
print(fav_lang)
# for stripping whitespaces from right side and use lstrip() to strip from left and simply strip() to remove whitespaces from both sides
print(fav_lang.rstrip()) 

# # Removing Prefixes:

nostarch_url = 'https://nostarch.com' 
new_url = nostarch_url.removeprefix('https://')
print(new_url)