from transformers import pipeline

token_classifier = pipeline("token-classification")

result = token_classifier("Bill Gates founded Microsoft")

print(result)
