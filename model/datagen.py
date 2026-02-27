import random
import pandas as pd

positive_texts = [
    "This product is amazing and works perfectly!",
    "Absolutely loved it, highly recommend!",
    "Very good quality for the price.",
    "I am extremely satisfied with my purchase.",
    "Fast delivery and excellent packaging.",
    "Exceeded my expectations, fantastic build quality.",
    "Customer service was very helpful and responsive.",
    "Superb product, will buy again!",
    "Worth every penny.",
    "Five stars, highly impressed!",
    "Really happy with this purchase.",
    "Top notch quality and performance.",
    "Brilliant product, works flawlessly.",
    "Great experience overall.",
    "Impressive quality and fast shipping."
]

negative_texts = [
    "Terrible product, stopped working in one day.",
    "Worst experience ever. Completely useless.",
    "This is a scam. Do not buy this!",
    "Fake product. Waste of money.",
    "Product broke after two uses. Very disappointed.",
    "Not worth the money. Poor quality.",
    "I regret buying this. Totally disappointed.",
    "Very bad quality and cheap material.",
    "Customer support never responded.",
    "Extremely dissatisfied with this purchase.",
    "Stopped working after a week.",
    "Poor packaging and damaged item.",
    "Not as described. Very misleading.",
    "Cheap and unreliable.",
    "Completely disappointed."
]

data = []

for _ in range(500):
    text = random.choice(positive_texts)
    rating = random.choice([4, 5])
    data.append([text, rating, 1])

for _ in range(500):
    text = random.choice(negative_texts)
    rating = random.choice([1, 2])
    data.append([text, rating, 0])

random.shuffle(data)

df = pd.DataFrame(data, columns=["text", "rating", "label"])
df.to_csv("training_data_1000.csv", index=False)

print("Dataset generated successfully!")