import streamlit as st
import pandas as pd

df = pd.DataFrame({
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
  "Employee24": 60000,
}
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.scatter_chart(df)
