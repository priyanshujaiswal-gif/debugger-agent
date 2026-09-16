import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()  # loads OPENAI_API_KEY from .env when running locally

if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

from agent import debug

st.title("🐛 Debugger Agent")

code = st.text_area("Paste your code", height=260, value='''def subtotal(items):
    total = 0
    for item in items:
        total += item["price"]
    return total''')

if st.button("Find the bug", type="primary"):
    with st.spinner("Thinking..."):
        st.markdown(debug(code))
