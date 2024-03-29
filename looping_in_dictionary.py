user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favortite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name, language in favortite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favortite_languages.keys():
    print(name.title())
for lang in favortite_languages.values():
    print(lang.title())
friends = ['phil', 'sarah']
for name in favortite_languages.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        language = favortite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    if 'erin' not in friends:
        print("Erin, please take our poll!")

for name in sorted(favortite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.\n")

print("The following languages have been mentioned:")
for lang in set(sorted(favortite_languages.values())):
    print(lang.title())
