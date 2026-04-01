from transformers import pipeline

fake_news = pipeline("text-classification", model="roberta-base-openai-detector")

text = input("Enter news: ")
print(fake_news(text))