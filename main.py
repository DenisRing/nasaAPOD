import requests
import streamlit as st

#API key, url
api_key = ""
url = "https://api.nasa.gov/planetary/apod?"\
      f"api_key={api_key}"

#get the request data as a dict
response1 = requests.get(url)
data = response1.json()

#image, title, url, explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

#download file
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
      file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)


