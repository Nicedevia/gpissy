from flask import Flask, render_template
import json, random

app = Flask(__name__)

def from_json():
    with open("appweb/data/scraped_data.json", "r") as f:
        for line in f:
            yield json.loads(line)

@app.route("/")
def random_quote():
    results = from_json()
    liste = list(results)
    random_quote = random.choice(liste)
    return render_template("code.html", item=random_quote)


if __name__ == '__main__':
    app.run(debug=True)

 