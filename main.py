import pandas as pd
import streamlit as st

st.title("Upload Excel File")
uploaded_file = st.file_uploader("Choose a file", type=["xlsx"])

if uploaded_file is not None:
    file = pd.read_excel(uploaded_file, sheet_name='Sheet1')
    st.subheader("Data Preview")
    st.write(file.head())
