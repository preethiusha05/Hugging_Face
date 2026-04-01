from transformers import pipeline

tts = pipeline("text-to-speech")

result = tts("Hello, welcome to NLP")