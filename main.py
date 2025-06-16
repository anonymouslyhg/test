import pandas as pd
import streamlit as st

st.title("Upload Excel File")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Rewind the file to start just to be safe
    uploaded_file.seek(0)
    
    # Read Excel using openpyxl engine
    file = pd.read_excel(uploaded_file, sheet_name='1', engine='openpyxl')
    
    st.subheader("Data Preview")
    st.write(file.head())
    d_info = file.info()
    st.text(d_info)


