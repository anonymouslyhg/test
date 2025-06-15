import streamlit as st
import pandas as pd

df = pd.DataFrame({"A" : [1,2], "B" : [3,4]})
st.subheader(df)
st.DataFrame(df)
st.Table(df)
st.json(df)
#st.header("header")
#st.subheader("subheader")
#st.text("text")
#st.code("print('python code')", language='python')
#st.markdown("**markdown**")
