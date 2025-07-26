# Basic Chatbot using if-else and loop

while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hi!")
    elif message == "how are you":
        print("Bot: I'm fine, thank you.")
    elif message == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
        