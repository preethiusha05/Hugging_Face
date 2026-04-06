from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love AI",
    "I like artificial intelligence",
    "I hate bugs"
]

embeddings = model.encode(sentences)

# Compare similarity
sim = cosine_similarity([embeddings[0]], embeddings)

print("Similarity Scores:", sim)