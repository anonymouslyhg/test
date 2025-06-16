import pandas as pd
import streamlit as st

# Load Excel file
file = pd.read_excel("D:/Python/patient information.xlsx", sheet_name='Sheet1')

# Show header
st.subheader("Patient Data Preview")
st.write(file.head())

# Show basic info manually (since file.info() doesn't return a DataFrame)
st.subheader("Data Information")
buffer = []
file.info(buf=buffer.append)
st.text(''.join(buffer))
