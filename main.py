from transformers import pipeline
from datasets import load_dataset

print("Loading models...\n")

# Models
zero_shot = pipeline("zero-shot-classification")
sentiment = pipeline("sentiment-analysis")
fill_mask = pipeline("fill-mask")

print("Models loaded!\n")

while True:
    print("\n=== Advanced NLP + Dataset Project ===")
    print("1. Zero-Shot Classification (User Input)")
    print("2. Sentiment Analysis (IMDb Dataset)")
    print("3. Fill Mask")
    print("4. News Classification (Dataset)")
    print("0. Exit")

    choice = input("Enter choice: ")

    # Zero-shot
    if choice == "1":
        text = input("Enter text: ")
        labels = input("Enter labels (comma separated): ").split(",")

        result = zero_shot(text, candidate_labels=labels)

        print("\nResult:")
        for l, s in zip(result["labels"], result["scores"]):
            print(f"{l} -> {round(s, 3)}")

    #  IMDb Dataset Sentiment
    elif choice == "2":
        print("\nLoading IMDb dataset...")
        dataset = load_dataset("imdb", split="test[:5]")

        for i, data in enumerate(dataset):
            text = data["text"]
            result = sentiment(text)

            print(f"\nReview {i+1}:")
            print(text[:100])
            print("Sentiment:", result)

    #  Fill Mask
    elif choice == "3":
        print("Use [MASK] token")
        text = input("Enter sentence: ")

        result = fill_mask(text)

        print("\nPredictions:")
        for r in result[:5]:
            print(r["sequence"], "->", round(r["score"], 3))

    #  News Dataset
    elif choice == "4":
        print("\nLoading AG News dataset...")
        dataset = load_dataset("ag_news", split="test[:5]")

        classifier = pipeline("text-classification")

        for i, data in enumerate(dataset):
            text = data["text"]
            result = classifier(text)

            print(f"\nNews {i+1}:")
            print(text)
            print("Prediction:", result)

    # Exit
    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")