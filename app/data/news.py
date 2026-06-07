
import json
import requests
import urllib

apikey = "29b7ca96572683201aa0e76b402535fb"
country = "in" #us, gb, fr, de, it, es, au, ca, cn, jp, in
category = "business" #general, world, nation, business, technology, entertainment, sports, science and health.
url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country={country}&max=10&apikey={apikey}"

def get_news():
    response = requests.get(url)
    data = json.loads(response.text)
    # print(data)
    return data

if __name__ == "__main__":
    get_news()
# articles = data["articles"]
# for i in range(len(articles)):
#     print(f"Title: {articles[i]['title']}")
#     print(f"Description: {articles[i]['description']}")