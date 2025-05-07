import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []
for quote in soup.select(".quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    quotes.append({"text": text, "author": author})

# Save to JSON
import json
with open("scraped_quotes.json", "w") as f:
    json.dump(quotes, f, indent=2)

print("Scraped data saved to scraped_quotes.json")
