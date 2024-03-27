# # Counting to twenty:

for value in range(1,21):
    print(value)

# # One Million:

for value in range(1,1_000_001):
    print(value)

# # Summing a Miilion:

million = [value for value in range(1,1_000_001)]
print(million)
print(min(million))
print(max(million))
print(sum(million))

# # Odd Numbers:

odd = [value for value in range(1,21,2)]
print(odd)

# # Threes:

threes = [value for value in range(3,31,3)]
print(threes)

# # Cubers:

cubes = [value**3 for value in range(1,11)]
print(cubes)