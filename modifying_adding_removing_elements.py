# # Modifying:

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# # Adding:

print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []             # APPEND METHOD
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles = ['honda','yamaha','suzuki']         # INSERT METHOD
motorcycles.insert(0,'ducati')
print(motorcycles)

# # Removing:

motocycles = ['honda','yamaha','suzuki']         # DEL METHOD
del motocycles[0]
print(motocycles)
motorcycles = ['honda','yamaha','suzuki']        # POP METHOD
print(motorcycles)
pop_motorcycles = motorcycles.pop()
print(pop_motorcycles)
print(motorcycles)
last_owned = motorcycles.pop(1)
print(f"The last motorcycle that i owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle i owned was a {first_owned.title()}.")
motorcycles = ['honda','yamaha','suzuki','honda']         # REMOVE METHOD 
print(motorcycles)
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive} is too expensive for me.")