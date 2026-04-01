from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

while True:
    user = input("You: ")
    if user == "exit":
        break

    response = chatbot(user, max_length=50)
    print("Bot:", response[0]['generated_text'])