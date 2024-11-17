def chatbot():
    print("Hello! I'm here to help you. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input and make it lowercase for case-insensitive matching
        user_input = input("You: ").lower()
        
        # Exit condition
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Responses based on keywords
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm a bot, so I don't have feelings, but thanks for asking! How can I help?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot, here to answer your queries.")
        
        elif "help" in user_input:
            print("Chatbot: Sure! Let me know what you need help with.")
        
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Feel free to come back if you have more questions.")
            break
        
        else:
            # Default response for unrecognized input
            print("Chatbot: I'm sorry, I don't understand that. Could you please rephrase?")
            
# Start the chatbot
chatbot()
