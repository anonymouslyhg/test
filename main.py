import pandas as pd
import streamlit as st

url = "https://drive.google.com/uc?export=download&id=1DJJd4WzTmRjTZBZmJPWhXE8-oRUDRyUE"

# Use error-handling and a safe parser
try:
    data = pd.read_csv(url, encoding='utf-8', engine='python')
    st.write(data.head())
except Exception as e:
    st.error(f"Error loading CSV: {e}")
