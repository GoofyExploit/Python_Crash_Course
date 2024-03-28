# # Buffet:

print('Original menu:')
basic_foods = ('bread','oats','khichadi','chapati','rice')
for food in basic_foods:
    print(food)

# basic_foods[0] = 'macroni'      # python does not support modification of tuples

print('\nRevised menu:')
basic_foods = ('bread','oats','khichadi','banana','curd')
for food in basic_foods:
    print(food)