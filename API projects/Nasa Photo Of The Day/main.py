import requests
import streamlit as sl

api_key = "K8xv7mY8lJNCgfPq4EY9aTbWVxvD6zXgDBgGH6nm"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

req = requests.get(url)

contents = req.json()

sl.title(f"{contents['title']}")
sl.image(contents["hdurl"])
content = contents["explanation"]
sl.info(content)