# # Conditional Tests:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

name = 'lucky'
print("Is name == 'lucky'? I predict True.")
print(name == 'lucky')
print("Is name == 'raghav'? I predict False.")
print(name == 'raghav')

fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')
print("Is fruit == 'mango'? I predict False.")
print(fruit == 'mango')

vegetable = 'ladyfinger'
print("Is vegetable == 'ladyfinger'? I predict True.")
print(vegetable == 'ladyfinger')
print("Is vegetable == 'potato'? I predict False.")
print(vegetable == 'potato')

sports = 'football'
print("Is sports == 'football'? I predict True.")
print(sports == 'football')
print("Is sports == 'cricket'? I predict False.")
print(sports == 'cricket')

# # More Conditional Test:

user = 'Lucky'
user1 = 'lucky'
num = 1
num1 = 3
name = 'Amit'
cities = ['london','sydney','tokyo']

if user == user1 or user != user1:
    print('True')
if num >= 0 and num1 >= 2:
    print('True')
if name.lower() == 'amit':
    print('True')
if 'london' in cities:
    print('True')
if 'berlin' not  in cities:
    print('True')
