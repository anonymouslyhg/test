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

# Convert dict to DataFrame with 2 columns: Employee and Salary
df = pd.DataFrame(list(salaries.items()), columns=["Employee", "Salary"])

# You need a correlation matrix with at least 2 numeric columns
# So we add a dummy numeric column to show heatmap purpose
df["Index"] = range(len(df))

# Compute correlation (only works on numeric columns)
fig, ax = plt.subplots()
sns.heatmap(df[["Salary", "Index"]].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
