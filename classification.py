from transformers import pipeline

classifier = pipeline("text-classification")

result = classifier("This is amazing!")
print("Classification:", result)