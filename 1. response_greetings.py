import re

def respond_to_greeting():
    responses = ["Hello!", "Hi there!", "Greetings!", "Nice to meet you!"]
    return responses

def respond_to_question(query):
    if re.search(r"\bhow are you\b", query, re.IGNORECASE):
        return "I'm just a computer program, but I'm here to help you!"
    elif re.search(r"\bwhat can you do\b", query, re.IGNORECASE):
        return "I can assist you with answering questions and providing information."
    else:
        return "I'm sorry, I don't understand that question."

def chatbot_response(user_input):
    if re.search(r"\b(?:hello|hi|hey)\b", user_input, re.IGNORECASE):
        return respond_to_greeting()
    else:
        return respond_to_question(user_input)

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: I'm sorry, I don't understand that.")
