# 🧠 Programming of Smart Devices - Python Project

## 📌 Overview

This project demonstrates the basics of Python programming through:

- Web scraping using `requests` and `BeautifulSoup`
- API integration with public endpoints (from JSONPlaceholder)
- Saving and reading data in JSON format
- Visualizing data using the Flask web framework

---

## 🧩 Project Structure
smart-devices-project/
- │
- ├─ scraper.py # Scraper for quotes website
- ├── api_app.py # Flask app for API data visualization
- ├── output.json # JSON output from API
- ├── scraped_quotes.json # JSON output from web scraper
- └── templates/
- └── index.html # Template for displaying data in browser

---

## ✅ Part 1: Web Scraping

- **File**: `scraper.py`
- **Website**: https://quotes.toscrape.com/
- **Libraries**:
  - `requests`: to fetch HTML
  - `beautifulsoup4`: to parse and extract content
- **What it does**:
  - Extracts quotes and their authors from the webpage
  - Saves the result into a file: `scraped_quotes.json`

---

## ✅ Part 2: API Integration + Flask Display

- **File**: `api_app.py`
- **API Used**: `https://jsonplaceholder.typicode.com/posts`
- **Libraries**:
  - `requests`: to make API requests
  - `flask`: to serve a web page showing API data
- **Functionality**:
  - Fetches API data and stores it in `output.json`
  - Displays the first 10 posts on a web page using `Flask` and `Jinja2` template (`index.html`)

---

## ⚙️ Setup & Run Instructions

### 1. Install Dependencies

```bash
pip install requests beautifulsoup4 flask
```
### 2. Run Web Scraper
```bash
python scraper.py
```
This will generate scraped_quotes.json with the extracted data.

### 2. Run Flask API App
```bash
python api_app.py
```
Then visit: http://127.0.0.1:5000

## 💾 Example Output
scraped_quotes.json
```json
[
  {
    "text": "“The world as we have created it is a process of our thinking...”",
    "author": "Albert Einstein"
  },
  ...
]
```
output.json
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati",
    "body": "quia et suscipit\nsuscipit..."
  },
  ...
]
```
## 📚 Learning Outcome
- Understood how to scrape data from HTML pages
- Learned to work with APIs and JSON in Python
- Built a Flask web app to visualize external data
- Learned how to structure a small full-stack Python project

## 📄 License
This project is created for educational purposes only. :)