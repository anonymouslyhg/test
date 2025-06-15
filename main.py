import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Avoid using 'dict' as a variable name (it's a built-in keyword)
salaries = {
    "Employee1": 55000,
    "Employee2": 62000,
    "Employee3": 48000,
    "Employee4": 71000,
    "Employee5": 53000,
    "Employee6": 59000,
    "Employee7": 60000,
    "Employee8": 64000,
    "Employee9": 58000,
    "Employee10": 50000,
    "Employee11": 66000,
    "Employee12": 54000,
    "Employee13": 62000,
    "Employee14": 57000,
    "Employee15": 69000,
    "Employee16": 55000,
    "Employee17": 63000,
    "Employee18": 56000,
    "Employee19": 61000,
    "Employee20": 52000,
    "Employee21": 67000,
    "Employee22": 58000,
    "Employee23": 59000,
    "Employee24": 60000
}

name = st.text_input("Enter Name: ")
num = st.number_input("Age: ", min_value=0, max_value=11)
box = st.checkbox("I agree ")
color = st.selectbox("Choose color ", ["Red","Green","Blue"])
button = st.button("Submit")
