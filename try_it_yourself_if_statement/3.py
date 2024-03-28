# # Hello Admin:

usernames = ['admin','jane','peter','david','harry']
for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

# # No users:

usernames = []
if usernames:
    for user  in usernames:
        print(f"Hello {user}, thank you for logging again!")
else:
    print("We need to find some users!")

# # Checking Usernames:

current_users = ['harry','jane','watson','black','shane','peter']
new_users = ['Peter','jane','mojo','pumpkin','hero','gin']
for users in new_users:
    if users.lower() in current_users: 
        print("Please, enter a new username!")
    else:
        print(f"Username '{users}' is available!")

# # Ordinal Numbers:

numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")