import requests
from urllib.parse import quote
from utils.logger import logger

API_KEY = "29b7ca96572683201aa0e76b402535fb"

def get_news(query,max_articles=10):
    url = f"https://gnews.io/api/v4/search?q={quote(query)}&lang=en&country=in&max={max_articles}&apikey={API_KEY}"
    logger.info(url)
    response = requests.get(url)
    logger.info(response.status_code)
    logger.info(response.text)
    response.raise_for_status()
    return response.json()

# if __name__ == "__main__":

#     news = get_news(query="Indian IT sector")

#     print(json.dumps(news, indent=2))
