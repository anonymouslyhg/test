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
import plotly.express as px
import streamlit as st

df = px.data.iris()

color_map = {
    'setosa': '#1f77b4',
    'versicolor': '#ff7f0e',
    'virginica': '#2ca02c'
}

fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                 color_discrete_map=color_map)
st.plotly_chart(fig)
import altair as alt
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'company': ['A', 'B', 'C', 'A', 'B', 'C'],
    'value': [10, 15, 8, 20, 14, 12]
})

color_scale = alt.Scale(domain=['A', 'B', 'C'], range=['#1f77b4', '#ff7f0e', '#2ca02c'])

chart = alt.Chart(df).mark_bar().encode(
    x='company',
    y='value',
    color=alt.Color('company', scale=color_scale)
)

st.altair_chart(chart)
