# NOVA — iPhone 18 Concept Store

A responsive Flask + HTML/CSS/JavaScript shopping-site concept with bold typography, neon gradients, CSS phone renders, product cards, and a working demo bag counter.

> Educational concept only. It is not an official Apple Store. Model details, availability, and prices are illustrative and should not be represented as real offers.

## Run locally / in GitHub Codespaces

```bash
pip install -r requirements.txt
python app.py
```

Open port 5000 in the Ports tab.

## Run with Docker commands

```bash
docker build -t nova-iphone-store .
docker run --rm -p 5000:5000 nova-iphone-store
```

Then open port 5000.
