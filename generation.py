from transformers import pipeline

generator = pipeline("text-generation")

result = generator("Artificial Intelligence is", max_length=30)

print("Text Generation:", result)