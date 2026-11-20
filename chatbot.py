# Basic Chatbot using Python

def chatbot():

    print("Chatbot: Hello! Welcome to my Chatbot.")

    while True:

        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi! How can I help you?")

        elif user == "hi":
            print("Chatbot: Hello! Nice to meet you.")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Chatbot: I am a Python Chatbot.")

        elif user == "thank you":
            print("Chatbot: You're welcome!")

        elif user == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")

# Calling the function
chatbot()
