from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

result = ner("Elon Musk is the CEO of Tesla.")
print("NER:", result)