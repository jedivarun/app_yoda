import streamlit as st
import requests

# Define the API endpoint
endpoint = "https://api.funtranslations.com/translate/yoda.json"

# Add the Yoda image
yoda_img = "https://vignette.wikia.nocookie.net/starwars/images/6/6f/Yoda_SWSB.png/revision/latest/top-crop/width/360/height/450?cb=20180906044831"

def yoda_translator(text):
    # Make a GET request to the endpoint with the text to translate
    response = requests.get(endpoint, params={"text": text})
    # Extract the translated text from the response
    data = response.json()
    yoda_text = data["contents"]["translated"]
    return yoda_text

st.title("Yoda Translator App")

# Show the Yoda image
st.image(yoda_img, width=200)

# Get text input from the user
text = st.text_input("Enter text to translate:")

# Translate the text and show the result
if st.button("Translate"):
    result = yoda_translator(text)
    st.success(result)

