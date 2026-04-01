from transformers import pipeline

translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = input("Enter text: ")
result = translator(text)

print("Translation:", result)