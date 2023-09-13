#defining function to replace empticons with emojis
def replace_emojis(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

# get user input
face = input("Enter emoticon ")

# Replace emoticons with emojis
result = replace_emojis(face)
print(result)
