from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("mood_dataset.csv")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    mood = request.form.get("mood")

    # Find recommendations for selected mood
    result = data[data["mood"].str.lower() == mood.lower()]

    if result.empty:
        return render_template(
            "index.html",
            error="No recommendations found for this mood."
        )

    # Select first recommendation
    recommendation = result.iloc[0]

    song = recommendation["song"]
    artist = recommendation["artist"]
    activity = recommendation["activity"]
    message = recommendation["motivation"]

    return render_template(
        "index.html",
        selected_mood=mood,
        song=song,
        artist=artist,
        activity=activity,
        message=message
)
if __name__ == "__main__":
    app.run(debug=True)