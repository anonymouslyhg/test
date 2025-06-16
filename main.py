import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = sns.load_dataset("tips")
sns.set_style("whitegrid")

st.set_page_config(page_title="🧠 Seaborn Visual Explorer", layout="wide")
st.title("📊 Seaborn Visualization Gallery")

chart_type = st.selectbox("Select a Chart Type", [
    "Scatterplot",
    "Barplot",
    "Lineplot",
    "Boxplot",
    "Violinplot",
    "Histogram + KDE",
    "Countplot",
    "Heatmap (Correlation)",
    "Pairplot",
    "LM Plot (Regression)",
    "Catplot",
    "Swarmplot",
    "Stripplot",
    "KDE Plot",
    "Jointplot",
    "Clustermap",
    "Combined Violin + Swarm",
])

st.subheader("Dataset Preview")
st.dataframe(df)

fig = plt.figure(figsize=(7, 4))

# Each chart rendering
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
    st.write("Generating pairplot...")
    pair_fig = sns.pairplot(df[["total_bill", "tip", "size"]])
    st.pyplot(pair_fig)

elif chart_type == "LM Plot (Regression)":
    st.write("Generating regression line plot...")
    lm_fig = sns.lmplot(x="total_bill", y="tip", data=df)
    st.pyplot(lm_fig)

elif chart_type == "Catplot":
    st.write("Bar-style catplot grouped by sex...")
    cat_fig = sns.catplot(x="day", y="total_bill", hue="sex", kind="bar", data=df)
    st.pyplot(cat_fig.fig)

elif chart_type == "Swarmplot":
    sns.swarmplot(x="day", y="total_bill", data=df)
    st.pyplot(fig)

elif chart_type == "Stripplot":
    sns.stripplot(x="day", y="total_bill", data=df, jitter=True)
    st.pyplot(fig)

elif chart_type == "KDE Plot":
    sns.kdeplot(df["total_bill"], shade=True)
    st.pyplot(fig)

elif chart_type == "Jointplot":
    st.write("Scatterplot with marginal histograms...")
    jp = sns.jointplot(x="total_bill", y="tip", data=df, kind="hex")
    st.pyplot(jp.fig)

elif chart_type == "Clustermap":
    st.write("Clustermap with correlation matrix...")
    cm_fig = sns.clustermap(df.corr(numeric_only=True), cmap="coolwarm", annot=True)
    st.pyplot(cm_fig.fig)

elif chart_type == "Combined Violin + Swarm":
    sns.violinplot(x="day", y="total_bill", data=df, inner=None, color=".8")
    sns.swarmplot(x="day", y="total_bill", data=df)
    st.pyplot(fig)

st.markdown("---")
st.info("Made with ❤️ by Streamlit + Seaborn")
