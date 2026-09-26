import streamlit as st
import streamlit.components.v1 as components

# Read your HTML file
with open("interface.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML content
components.html(html_content, height=600, scrolling=True)
