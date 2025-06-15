import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = sns.load_dataset("tips")
sns.set_style("whitegrid")

st.set_page_config(page_title="Seaborn Charts Demo", layout="wide")
st.title("📊 Seaborn Charts in Streamlit")

chart_type = st.selectbox("Choose a chart to display:", [
    "Scatterplot",
    "Barplot",
    "Lineplot",
    "Boxplot",
    "Violinplot",
    "Histogram + KDE",
    "Countplot",
    "Heatmap (Correlation)",
    "Pairplot",
    "LM Plot (Regression)"
])

st.write("Dataset Preview:")
st.dataframe(df)

fig = plt.figure(figsize=(7, 4))

# Plot based on selection
if chart_type == "Scatterplot":
    sns.scatterplot(x="total_bill", y="tip", data=df)
    st.pyplot(fig)

elif chart_type == "Barplot":
    sns.barplot(x="day", y="total_bill", data=df)
    st.pyplot(fig)

elif chart_type == "Lineplot":
    sns.lineplot(x="size", y="total_bill", data=df)
    st.pyplot(fig)

elif chart_type == "Boxplot":
    sns.boxplot(x="day", y="total_bill", data=df)
    st.pyplot(fig)

elif chart_type == "Violinplot":
    sns.violinplot(x="day", y="total_bill", data=df)
    st.pyplot(fig)

elif chart_type == "Histogram + KDE":
    sns.histplot(df["total_bill"], bins=10, kde=True)
    st.pyplot(fig)

elif chart_type == "Countplot":
    sns.countplot(x="day", data=df)
    st.pyplot(fig)

elif chart_type == "Heatmap (Correlation)":
    fig = plt.figure(figsize=(8, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    st.pyplot(fig)

elif chart_type == "Pairplot":
    st.write("This will open multiple plots...")
    pair_fig = sns.pairplot(df[["total_bill", "tip", "size"]])
    st.pyplot(pair_fig)

elif chart_type == "LM Plot (Regression)":
    lm_fig = sns.lmplot(x="total_bill", y="tip", data=df)
    st.pyplot(lm_fig)

st.markdown("---")
st.info("Made with ❤️ using Streamlit and Seaborn")
