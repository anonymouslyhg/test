import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Upload Excel File")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Rewind the file to start just to be safe
    uploaded_file.seek(0)
    fig = plt.figure(2,2, figsize=(7,3))
    # Read Excel using openpyxl engine
    file = pd.read_excel(uploaded_file, sheet_name='1', engine='openpyxl')
    gender = file["gender"].map({0: 'Female', 1: 'Male'})
    gen_counts = gender.value_counts()
    gen_num = np.array(gen_counts.values)
    labels = gen_counts.index
    plt.pie(gen_num, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

