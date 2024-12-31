import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! What's on your mind?",
    "hey": "Hey! How's it going?",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Goodbye! See you later!",
    "add": "What numbers would you like to add?",
    "subtract": "What numbers would you like to subtract?",
    "multiply": "What numbers would you like to multiply?",
    "divide": "What numbers would you like to divide?",
    "introduce": "My name is Chatbot, I'm here to help you with any questions or tasks you may have.",
    "joke": "Why was the math book sad? Because it had too many problems.",
    "weather": "How's the weather like today?",
    "hobby": "What's your favorite hobby?",
    "help": "I'm not sure I understand what you mean. Can you please rephrase or provide more context?"
}


def process_input(input_text):
    doc = nlp(input_text)
    for token in doc:
        if token.text.lower() in responses:
            return responses[token.text.lower()]
        elif token.pos_ == "NUM":
            return "You entered a number. What would you like to do with it?"
        else:
            return "I didn't understand that. Can you please rephrase?"


def perform_arithmetic(input_text):
    try:
        doc = nlp(input_text)
        numbers = [token.text for token in doc if token.pos_ == "NUM"]
        operation = [token.text for token in doc if token.text.lower() in ["add", "subtract", "multiply", "divide"]][0]
        if operation == "add":
            result = sum([float(num) for num in numbers])
        elif operation == "subtract":
            result = float(numbers[0]) - sum([float(num) for num in numbers[1:]])
        elif operation == "multiply":
            result = 1
            for num in numbers:
                result *= float(num)
        elif operation == "divide":
            if len(numbers) < 2:
                return "Please provide two numbers to divide."
            if float(numbers[1]) == 0:
                return "Cannot divide by zero."
            result = float(numbers[0]) / float(numbers[1])
        return f"The result of the operation is {result}."
    except Exception as e:
        return "I apologize, I couldn't process that operation. Please try again."


def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = process_input(user_input)
        if response in responses.values():
            print("Chatbot:", response)
        elif "You entered a number" in response:
            print("Chatbot:", response)
            user_input = input("You: ")
            print("Chatbot:", perform_arithmetic(user_input))
        else:
            print("Chatbot:", perform_arithmetic(user_input))


chatbot()