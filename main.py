import streamlit as st
import pandas as pd

df = pd.DataFrame({"A" : [1,2], "B" : [3,4]})

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.scatter_chart(df)
st.map(df)
