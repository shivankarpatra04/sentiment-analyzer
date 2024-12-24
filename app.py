from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    if request.method == "POST":
        user_input = request.form.get("text_input")
        if user_input:
            analysis = TextBlob(user_input)
            if analysis.sentiment.polarity > 0:
                sentiment = "Positive"
            elif analysis.sentiment.polarity == 0:
                sentiment = "Neutral"
            else:
                sentiment = "Negative"
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
