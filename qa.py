from transformers import pipeline

qa = pipeline("question-answering")

result = qa(
    question="Who is the CEO of Tesla?",
    context="Elon Musk is the CEO of Tesla."
)

print("QA:", result)