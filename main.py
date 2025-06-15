import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.download("Download", data="Content of Data", file_name="data.txt")
st.write("Donwloader")
