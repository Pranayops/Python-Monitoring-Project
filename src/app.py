
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    products = [
        {
            "name": "iPhone 18 Pro",
            "storage": "256 GB",
            "price": "₹1,64,900",
            "image": "https://placehold.co/400x400/eeeeee/222222?text=iPhone+18+Pro"
        },
        {
            "name": "iPhone 18 Pro Max",
            "storage": "256 GB",
            "price": "₹1,79,900",
            "image": "https://placehold.co/400x400/eeeeee/222222?text=iPhone+18+Pro+Max"
        }
    ]

    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)