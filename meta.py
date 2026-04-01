from transformers import pipeline

toxic = pipeline("text-classification", model="unitary/toxic-bert")

text = input("Enter comment: ")
result = toxic(text)

print(result)