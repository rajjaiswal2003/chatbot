from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

# Function to format text to Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Configure the API key for the Gemini model
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Function to load OpenAI model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    system_instruction="You are a ChatBot named yatri, your task is to answers all the queries related to Sustainable Development and sustainable development goals. If a question is unrelated to Sustainable Development, answer \"Please  ask questions only related to sustainable  development.\"",
    )

    chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hi",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hello! 👋  I'm yatri, your guide to all things sustainable development. What can I help you learn about today? 🌎 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Who is PM of India\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please ask questions only related to sustainable development. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "What is a car",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please ask questions only related to sustainable development. \n",
      ],
    },
  ]
)

    response = chat_session.send_message(question)

    return response.text
    

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
