# # T-Shirt:

def make_shirt(size,text):
    # size = input("Enter the size of your T-shirt: "")
    # text = input("Enter the text you want to be printed on your T-Shirt: ")
    print(f"Your T-Shirt's size is {size}, and the text you want is '{text}'.")
make_shirt(size=8,text="Don't Give Up!")

# # Large Shirts:

def make_shirt(size='Large',text='I love python'):
    print(f"Your Shirt's Size is {size}, and text is '{text}'.")
make_shirt()

# # Cities:

def describe_city(city,country='japan'):
    print(f"{city.title()} is in {country.title()}.")
describe_city(city='japan')
describe_city(city='osaka')
describe_city(city='berlin',country='germany')