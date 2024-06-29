# app.py
import streamlit as st
from main import Summarizer

# Initialize the summarizer
summarizer = Summarizer()

# Streamlit app
st.title("Text Summarization App")
st.write("Enter the text you want to summarize below:")

user_input = st.text_area("Input Text", height=200)

if st.button("Summarize"):
    if user_input:
        summary = summarizer.summarize(user_input)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")
