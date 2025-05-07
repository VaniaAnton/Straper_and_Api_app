import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()

    with open("output.json", "w") as f:
        json.dump(data, f, indent=2)

    return render_template("index.html", posts=data[:10])  # Display 10 items

if __name__ == "__main__":
    app.run(debug=True)
