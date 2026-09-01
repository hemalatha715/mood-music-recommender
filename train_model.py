import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

import pickle


# Load dataset
data = pd.read_csv("mood_dataset.csv")

# Input text
X = data["text"]

# Mood labels
y = data["mood"]


# Create Machine Learning model
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)


# Train the model
model.fit(X, y)


# Save trained model
with open("mood_model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Mood prediction model trained successfully!")