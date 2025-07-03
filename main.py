import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

df = sns.load_dataset('iris')

palette = {
    'setosa': '#1f77b4',
    'versicolor': '#ff7f0e',
    'virginica': '#2ca02c'
}

fig, ax = plt.subplots()
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', palette=palette, ax=ax)
st.pyplot(fig)
