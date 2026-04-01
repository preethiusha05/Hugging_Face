from transformers import pipeline

summarizer = pipeline("summarization")

text = """Hugging Face provides powerful NLP tools using transformers 
models that can perform multiple tasks easily."""

result = summarizer(text, max_length=30, min_length=10)

print("Summary:", result)