# # Rivers:

rivers = {
    'nile':'egypt',
    'coorg':'karnataka',
    'chamba':'himachal pradesh',
}
for river, location in rivers.items():
    print(f"\nThe {river.title()} runs through {location.title()}.")
print("\nRivers mentioned are:")
for river in rivers.keys():
    print(river.title())
print("\nLocations mentioned are:")
for location in rivers.values():
    print(location.title())

# # Polling:

favortite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'java',
}
dev = ['jen','sarah']
dev1 = ['peter','rock']
for people in dev:
    print(f"\n{people.title()}, thank you for taking the poll!")
for people in dev1:
    print(f"\n{people.title()}, please take our poll!")
