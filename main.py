import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

api_key = os.getenv("NEWSAPI_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&" \
      f"from=2023-06-27&sortBy=publishedAt&apiKey={api_key}"


request = requests.get(url)

# Get dictionary with data
content = request.json()

body = ""

for article in content["articles"]:
    if article['title'] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2* "\n"

body = body.encode("utf-8")
send_email(message=body)