import streamlit as st
import requests

def send_message(message, endpoint_url):
    # Make an API request to the endpoint with the user's message
    response = requests.post(endpoint_url, json={'message': message})

    # Extract and return the response text from the API
    return response.json().get('response', 'Error: No response')

# Streamlit app layout
st.title('Chat Application')

# User input box for message
user_input = st.text_input('Enter your message:')

# User input box for endpoint URL
endpoint_url = st.text_input('Enter API Endpoint URL:')
st.write(f'Using API Endpoint: {endpoint_url}')

if st.button('Send'):
    # When the user clicks the "Send" button, send the message to the API
    response_text = send_message(user_input, endpoint_url)

    # Display the response in a chat-like format
    st.text_area('Bot:', response_text, height=100)
