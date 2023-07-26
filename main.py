import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWSAPI_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&" \
      f"from=2023-06-26&sortBy=publishedAt&apiKey={api_key}"


request = requests.get(url)

# Get dictionary with data
content = request.json()

for article in content["articles"]:
    print(article["title"])