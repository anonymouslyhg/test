import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

fig = px.scatter(df, x="A", y="B", color="C")
st.plotly_chart(fig)

st.write("good")
