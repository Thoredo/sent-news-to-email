import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

topic = "marvel"

api_key = os.getenv("NEWSAPI_API_KEY")
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      f"from=2023-06-27&sortBy=publishedAt&apiKey={api_key}" \
      "&language=en"


request = requests.get(url)

# Get dictionary with data
content = request.json()

body = "Subject: Today's news" + "\n"

keys_we_use = ["title", "description", "url"]

for article in content["articles"][:20]:
    if all(article[key] is not None for key in keys_we_use):
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2* "\n"

body = body.encode("utf-8")
send_email(message=body)