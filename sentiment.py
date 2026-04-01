from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

result = sentiment("I love learning NLP!")
print("Sentiment:", result)