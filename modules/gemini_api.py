import streamlit as st
import google.generativeai as genai

# Use Streamlit secrets in Cloud deployment for API key
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found! Please add GOOGLE_API_KEY in Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text
