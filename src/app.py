from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {"name": "iPhone 18 Pro", "tag": "PRO POWER", "storage": "256 GB", "price": "Concept price · ₹1,64,900", "color": "#b9a4e8", "badge": "MOST LOVED"},
    {"name": "iPhone 18 Pro Max", "tag": "BIG SCREEN ENERGY", "storage": "512 GB", "price": "Concept price · ₹1,79,900", "color": "#8b82d8", "badge": "MAX EXPERIENCE"},
    {"name": "iPhone 18", "tag": "YOUR NEXT ICON", "storage": "256 GB", "price": "Concept price · ₹1,34,900", "color": "#6da9f8", "badge": "FRESH DROP"},
]

@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
