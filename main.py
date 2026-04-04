from transformers import pipeline
from datasets import load_dataset

print("Loading models...\n")

# Load models
zero_shot = pipeline("zero-shot-classification")
fill_mask = pipeline("fill-mask")
sentiment = pipeline("sentiment-analysis")

print("Models loaded successfully!\n")

while True:
    print("\n=== NLP Project (All Dataset-Based) ===")
    print("1. Zero-Shot Classification (Dataset)")
    print("2. Sentiment Analysis (IMDb Dataset)")
    print("3. Fill Mask (Dataset-Based)")
    print("4. News Classification (Dataset)")
    print("0. Exit")

    choice = input("Enter choice: ")

    # Zero-Shot using dataset
    if choice == "1":
        print("\nLoading AG News dataset...")
        dataset = load_dataset("ag_news", split="test[:5]")

        labels = ["World", "Sports", "Business", "Technology"]

        for i, data in enumerate(dataset):
            text = data["text"]
            result = zero_shot(text, candidate_labels=labels)

            print(f"\nText {i+1}:")
            print(text)
            print("Top Prediction:", result["labels"][0], "->", round(result["scores"][0], 3))

    #  IMDb Sentiment
    elif choice == "2":
        print("\nLoading IMDb dataset...")
        dataset = load_dataset("imdb", split="test[:5]")

        for i, data in enumerate(dataset):
            text = data["text"]
            result = sentiment(text)

            print(f"\nReview {i+1}:")
            print(text[:100])
            print("Sentiment:", result)

    #  Fill Mask using dataset
    elif choice == "3":
        print("\nLoading AG News dataset...")
        dataset = load_dataset("ag_news", split="test[:5]")

        for i, data in enumerate(dataset):
            text = data["text"]

            # Take first word and create mask sentence
            first_word = text.split()[0]

            sentence = f"{first_word} is [MASK]."

            print(f"\nInput {i+1}: {sentence}")

            result = fill_mask(sentence)

            print("Predictions:")
            for r in result[:3]:
                print(r["sequence"], "->", round(r["score"], 3))

    #  News Classification
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
        print("Exiting... ")
        break

    else:
        print("Invalid choice!")