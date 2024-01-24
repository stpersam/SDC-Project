import streamlit as st
import requests
import os

API_URL = os.environ['API_URL']

def send_message(message):
    # Make an API request to the endpoint with the user's message
    response = requests.get(API_URL+"/get_text?prompt="+message)
    # Extract and return the response text from the API
    return response.json().get('text', 'Error: No response')

# Streamlit app layout
st.title('Chat Application')

# User input box for message
user_input = st.text_input('Enter your message:')


if st.button('Send'):
    # When the user clicks the "Send" button, send the message to the API
    response_text = send_message(user_input)

    # Display the response in a chat-like format
    st.text_area('Bot:', response_text, height=100)
