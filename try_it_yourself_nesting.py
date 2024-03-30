# # People:

friends = {
    'luckyg':{
        'first':'lucky',
        'last':'grover',
    },
    'dhruvs':{
        'first':'dhruv',
        'last':'suneja',
    },
    'kartikj':{
        'first':'kartik',
        'last':'jindal',
    }
}

for friend, info in friends.items():
    print(f"\nFriend: {friend}")
    full_name = f"{info['first']} {info['last']}"
    print(f"Full name: {full_name}")

# # Pets:

bruno = {
    'kind':'dog',
    'owner':'Lucky',
}
pussy = {
    'kind':'cat',
    'owner':'Lucky',
}
sherkhan = {
    'kind':'lion',
    'owner':'Lucky',
}
pets = [bruno, pussy, sherkhan]
for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner: {pet['owner']}")
    print()

# # favorite Numbers:

favorite_places = {
    'lucky':'vrindavan',
    'dhruv':'mathura',
    'kartik':'ayodhya',
}
for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite place is {places.title()}.")

# Favorite Numbers:

favorite_number = {
    'lucky':69,
    'dhruv':15,
    'kartik':45,
}
for person, number in favorite_number.items():
    print(f"{person.title()}'s favorite number is {number}.")

# # Cities:

cities = {
    'tokyo':{
        'country':'japan',
        'population':'1.4 crores',
        'fact':'aesthetic',
    },
    'sydney':{
        'country':'australia',
        'population':'53.1 lakhs',
        'fact':'luxury', 
    },
    'berlin':{
        'country':'germany',
        'population':'36.4 lakhs',
        'fact':'urban centre of germany'
    }
}
for city, info in cities.items():
    print(f"\nCity Name: {city.title()}") 
    info_1 = f"{info['country']}"
    info_2 = f"{info['population']}"
    info_3 = f"{info['fact']}"
    print(f"Info:\n\tCountry: {info_1.title()}")
    print(f"\tPopulation: {info_2.title()}")
    print(f"\tFact: {info_3.title()}")