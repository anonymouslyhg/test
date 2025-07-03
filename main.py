import pandas as pd
import streamlit as st
url = "https://drive.google.com/file/d/1DJJd4WzTmRjTZBZmJPWhXE8-oRUDRyUE/view?usp=sharing"
file = pd.read_csv(url)
st.write(file)
