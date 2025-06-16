import pandas as pd
import streamlit as st

st.title("Upload Excel File")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Specify engine explicitly to avoid stream handling errors
    file = pd.read_excel(uploaded_file, sheet_name='Sheet1', engine='openpyxl')
    
    st.subheader("Data Preview")
    st.write(file.head())
