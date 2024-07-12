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

# Function to load OpenAI model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    
    # Define sustainability-related keywords
    sustainability_keywords = [
        "sustainability", "climate change", "environment", "renewable energy",
        "recycling", "carbon footprint", "greenhouse gases", "eco-friendly",
        "sustainable", "conservation", "biodiversity", "green technology"
    ]
    
    # Check if the question is related to sustainability
    if any(keyword.lower() in question.lower() for keyword in sustainability_keywords):
        prompt = f"Please provide detailed and accurate information on sustainability-related topics.\n\nQuestion: {question}\n\nResponse:"
        response = model.generate_content(prompt)
        return response.text
    else:
        return "Please ask a sustainability-related question."

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
