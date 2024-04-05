# # Messages:

msg = ['hello','hi','bye','wyd']
def show_messages():
    for message in msg:
        print(message)
show_messages()

# # Sending Messages:

show_message = ['hello','hi','bye','wyd']
sent_messages = []
def send_messages():
    while show_message:
        current_msg = show_message.pop()
        print(current_msg)
        sent_messages.append(current_msg)
send_messages()
print(f"Original List: {show_message}")
print(f"New List: {sent_messages}")

# # Archived Messages:

show_message = ['hello','hi','bye','wyd']
sent_messages = []
def send_messages(show_message,sent_messages):
    while show_message:
        current_msg = show_message.pop()
        print(current_msg)
        sent_messages.append(current_msg)
send_messages(show_message[:],sent_messages)
print(f"Original List: {show_message}")
print(f"New List: {sent_messages}")