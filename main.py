import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Load dataset
df = sns.load_dataset('iris')

# Define consistent color palette
palette = {
    'setosa': '#1f77b4',
    'versicolor': '#ff7f0e',
    'virginica': '#2ca02c'
}

st.title("Iris Dataset Visualizations with Consistent Colors")

# Dropdown for chart selection
chart_type = st.selectbox("Choose Chart Type", ['Scatter', 'Line', 'Box', 'Bar (Mean)', 'Pair Plot'])

fig, ax = plt.subplots()

if chart_type == 'Scatter':
    sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', palette=palette, ax=ax)
    st.pyplot(fig)

elif chart_type == 'Line':
    sns.lineplot(data=df.sort_values(by='sepal_length'), x='sepal_length', y='petal_length', hue='species', palette=palette, ax=ax)
    st.pyplot(fig)

elif chart_type == 'Box':
    sns.boxplot(data=df, x='species', y='sepal_length', palette=palette, ax=ax)
    st.pyplot(fig)

elif chart_type == 'Bar (Mean)':
    grouped = df.groupby('species').mean(numeric_only=True).reset_index()
    sns.barplot(data=grouped, x='species', y='sepal_length', palette=palette, ax=ax)
    st.pyplot(fig)

elif chart_type == 'Pair Plot':
    st.write("Note: Pair plot opens in a separate figure")
    pair_fig = sns.pairplot(df, hue='species', palette=palette)
    st.pyplot(pair_fig)
