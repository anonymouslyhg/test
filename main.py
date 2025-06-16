import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

st.set_page_config(page_title="Seaborn Graphs", layout="wide")
st.title("Seaborn Demo")

fig = plt.figure(figsize=(4, 1))
sns.kdeplot(df["total_bill"])
st.pyplot(fig)

st.header("Hello")
