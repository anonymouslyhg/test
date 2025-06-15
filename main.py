import streamlit as st
import pandas as pd

df = pd.DataFrame({"A" : [1,2], "B" : [3,4]})

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.scatter_chart(df)
st.map(df)
#st.subheader(df)
#st.dataframe(df)
#st.table(df)
#st.json(df)
#st.header("header")
#st.subheader("subheader")
#st.text("text")
#st.code("print('python code')", language='python')
#st.markdown("**markdown**")
