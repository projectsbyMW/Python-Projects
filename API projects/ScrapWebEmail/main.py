import requests
from sendemail import sendemail
from datetime import date
from datetime import timedelta


topic = "taylor-swift"

yesterday = date.today() - timedelta(days = 1)

api_key = "a6cbc35f8e86403ebf32316e10c6a3f8"

url = "https://newsapi.org/v2" \
    f"/everything?q={topic}" \
    f"&from={yesterday}&" \
    "sortBy=popularity&apiKey=" \
    "a6cbc35f8e86403ebf32316e10c6a3f8&" \
    "language=en"

req = requests.get(url)

content = req.json()

string = "Subject: WEBAPI Project Results \n\n"

for article in content["articles"]:
    if article["title"] not in [None,"[Removed]"]:
        message = str(article["title"])+ " - " + str(article["source"]["name"]) + "\n" + str(article["url"]) + "\n"*2 
        string += message

string = string.encode("utf-8")

sendemail(string)
