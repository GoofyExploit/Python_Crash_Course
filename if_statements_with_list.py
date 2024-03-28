requested_toppings = ['mushrooms','green peppers','extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print(f"Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for toppings in requested_toppings:
    if toppings in available_toppings:
        print(f"Adding {toppings}")
    else:
        print(f"Sorry, we don't have {toppings}.")

print("\nFinished making your pizza!")