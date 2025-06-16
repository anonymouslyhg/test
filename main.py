import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

st.set_page_config(page_title="Seaborn Graphs", layout="wide")
st.title("Seaborn Demo")

fig, ax = plt.subplots(figsize=(7, 3))
sns.lineplot(x="total_bill", y="tip",hue="region", data=df, ax=ax)
st.pyplot(fig)

st.header("Hello")
