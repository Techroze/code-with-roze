# Get user input
answer = input("Greetings: ")

new_answer = answer.lower().strip()

# Check if user says hello
if 'hello' in new_answer:
    print("$0")

# Check if answer starts with 'h', print $20
elif 'h' == new_answer[0]:
    print("$20")

# Otherwise, print $100
else:
    print("$100")