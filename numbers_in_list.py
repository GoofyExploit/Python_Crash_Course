for value in range(6):      # Range function
    print(value)

numbers = list(range(1,6))    # List function
print(numbers)

even_numebers = list(range(2,11,2))     # third argument to skip interval
print(even_numebers)

squares = []              # squares from 1 to 10 in a list
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]      # some functions to deal with numbers in a list
print(min(digits))
print(max(digits))
print(sum(digits))