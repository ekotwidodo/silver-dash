import streamlit as st

def load_map():
  # URL dari halaman web yang ingin dimuat
  url = "https://datawrapper.dwcdn.net/0I7dO/1/"
  # Menampilkan halaman web dalam iframe di Streamlit
  st.components.v1.iframe(src=url, width=800, height=400, scrolling=True)