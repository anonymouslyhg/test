import pandas as pd
import streamlit as st

st.title("Upload Excel File")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Rewind the file to start just to be safe
    uploaded_file.seek(0)
    
    # Read Excel using openpyxl engine
    file = pd.read_excel(uploaded_file, sheet_name='1', engine='openpyxl')
    gender = file["gender"].map({0: 'Female', 1: 'Male'})
    st.text(gender[1])

