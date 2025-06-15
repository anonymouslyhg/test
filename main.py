import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.sidebar.title("Gamer")
st.sidebar.radio("Option",["A","B","C"])
col1, col2 = st.columns(2)

with col1:
  st.write("Left Columns")
with col2:
  st.write("Right Colimns")

st.expander("See More").write("Hided Content")
