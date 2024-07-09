import streamlit as st
import pyshorteners as pyst
import pyperclip

shortener = pyst.Shortener()

def copy_to_clipboard():
  pyperclip.copy(shorted_url)

st.markdown("<h1 style='text-align: center;'>URL SHORTENER</h1>", unsafe_allow_html=True)
form = st.form("name")
url = form.text_input("URL HERE")
submit_btn = form.form_submit_button("Shorten url")

if submit_btn:
  shorted_url = shortener.tinyurl.short(url)
  st.markdown("<h3>Shorted url:</h3>", unsafe_allow_html=True)
  st.markdown(f"<h6 style='text-align: center;'>{shorted_url}</h6>", unsafe_allow_html=True)
  st.button("copy", on_click=copy_to_clipboard)