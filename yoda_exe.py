import streamlit as st
import requests

# Define the API endpoint
endpoint = "https://api.funtranslations.com/translate/yoda.json"

def yoda_translator(text):
    # Make a GET request to the endpoint with the text to translate
    response = requests.get(endpoint, params={"text": text})
    # Extract the translated text from the response
    data = response.json()
    yoda_text = data["contents"]["translated"]
    return yoda_text

st.title("Yoda Translator App")

# Get text input from the user
text = st.text_input("Enter text to translate:")

# Translate the text and show the result
if st.button("Translate"):
    result = yoda_translator(text)
    st.success(result)
