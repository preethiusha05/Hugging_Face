from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

print("Loading model...\n")
model = SentenceTransformer('all-MiniLM-L6-v2')

data = [
    "Apple is a fruit",
    "Mango is sweet fruit",
    "Car is a vehicle",
    "Bike is a two wheeler",
    "Python is a programming language",
    "Machine learning is AI"
]

labels = ["fruit", "fruit", "vehicle", "vehicle", "tech", "tech"]

embeddings = model.encode(data).astype('float32')

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

print("System Ready!\n")

query = input("Enter your search query: ")

query_vec = model.encode([query]).astype('float32')

distances, indices = index.search(query_vec, k=3)

print("\nTop Results:\n")

for i in indices[0]:
    print("Text:", data[i])
    print("Category:", labels[i])
    print("-----")

choice = input("\nDo you want to filter by category? (yes/no): ")

if choice.lower() == "yes":
    category = input("Enter category (fruit/vehicle/tech): ")

    print("\nFiltered Results:\n")
    for i in indices[0]:
        if labels[i] == category:
            print("Text:", data[i])