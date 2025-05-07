import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()

    # Save data to output.json
    with open("output.json", "w") as f:
        json.dump(data, f, indent=2)

    return render_template("index.html", fact=data["fact"])

if __name__ == "__main__":
    app.run(debug=True)
