import base64
import matplotlib.pyplot as plt
import streamlit as st
import re

def download_text_file(text, label="Download Report"):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="report.txt">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

def draw_pie_chart(match_percentage):
    fig, ax = plt.subplots()
    labels = ['Match', 'Remaining']
    sizes = [match_percentage, 100 - match_percentage]
    colors = ['#20c997', '#e64980']
    explode = (0.1, 0)
    ax.pie(
        sizes, explode=explode, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90
    )
    ax.axis('equal')
    return fig

def extract_match_percentage(response_text):
    match = re.search(r"Match (?:Rate|Percentage):\s*(\d+)%", response_text)
    return int(match.group(1)) if match else 0
