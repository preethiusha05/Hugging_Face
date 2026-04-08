from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from datasets import load_dataset

print("Loading dataset...\n")

dataset = load_dataset("ag_news", split="train[:200]")

texts = [data["text"] for data in dataset]
labels = [data["label"] for data in dataset]

label_names = ["World", "Sports", "Business", "Sci/Tech"]

print("Loading model...\n")
model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode(texts).astype('float32')

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

print("System Ready!\n")

query = input("Enter your search query: ")

query_vec = model.encode([query]).astype('float32')

distances, indices = index.search(query_vec, k=5)

print("\nTop Results:\n")

for rank, i in enumerate(indices[0]):
    
    score = 1 / (1 + distances[0][rank])

    print(f"Rank {rank+1}")
    print("Text:", texts[i][:150])
    print("Category:", label_names[labels[i]])
    print("Similarity Score:", round(score, 3))
    print("-----")

choice = input("\nDo you want to filter by category? (yes/no): ")

if choice.lower() == "yes":
    category = input("Enter category (World/Sports/Business/Sci/Tech): ")

    print("\nFiltered Results:\n")
    for rank, i in enumerate(indices[0]):
        if category.lower() in label_names[labels[i]].lower():
            print("Text:", texts[i][:150])
            print("Category:", label_names[labels[i]])
            print("-----")