#Display question and receive input

user_input = input("What is the answer to the Great Question of life, the Universe, and Everything? ")
# check if input is equal to answer or not if not print no
if user_input.lower().strip() in ["42", "forty two", "forty-two"]:
    print("Yes")
else:
    print("No")