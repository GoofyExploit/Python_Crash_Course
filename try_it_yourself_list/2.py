# # Guest List:

invite = ['amit','prashant','kanav']
print(f"I would like to invite {invite[0].title()} for dinner.")
print(f"I would like to invite {invite[1].title()} for dinner.")
print(f"I would like to invite {invite[2].title()} for dinner.")

# # Changing Guest List:

invite = ['amit','prashant','kanav']
not_available = 'kanav'
invite.remove('kanav')
print(not_available)
print(invite)
new_list = invite.append('anvit')
print(f"I would like to invite {invite[0].title()} for dinner.")
print(f"I would like to invite {invite[1].title()} for dinner.")
print(f"I would like to invite {invite[2].title()} for dinner.")

# # More Guests:

invite = ['amit','prashant','kanav']
print('So, everybody to your kind there are three new guests coming to our dinner tonight !!')
invite.insert(0,'anvit')
invite.insert(2,'parth')
invite.insert(5,'dhruv')
print(f"I would like to invite {invite[0].title()} for dinner.")
print(f"I would like to invite {invite[1].title()} for dinner.")
print(f"I would like to invite {invite[2].title()} for dinner.")
print(f"I would like to invite {invite[3].title()} for dinner.")
print(f"I would like to invite {invite[4].title()} for dinner.")
print(f"I would like to invite {invite[-1].title()} for dinner.")

# # Shrinking Guest List:

print('Sorry guys, i can only invite 2 people for dinner.')
not_invited1 = invite.pop()
print(f"Sorry {not_invited1.title()}, i can't invite you to dinner tonight.")
not_invited2 = invite.pop()
print(f"Sorry {not_invited2.title()}, i can't invite you to dinner tonight.")
not_invited3 = invite.pop()
print(f"Sorry {not_invited3.title()}, i can't invite you to dinner tonight.")
not_invited4 = invite.pop()
print(f"Sorry {not_invited4.title()}, i can't invite you to dinner tonight.")
print(f"Congrats {invite[0].title()}, you are invited tonight.")
print(f"Congrats {invite[1].title()}, you are invited tonight.")
del invite[0]
del invite[0]
print(invite)