import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


name = st.text_input("Enter Name: ")
num = st.number_input("Age: ", min_value=0, max_value=11)
box = st.checkbox("I agree ")
color = st.selectbox("Choose color ", ["Red","Green","Blue"])
button = st.button("Submit")
