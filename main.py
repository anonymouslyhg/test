import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page setup
st.set_page_config(page_title="All Matplotlib Features in Streamlit", layout="wide")
st.title("📊 Complete Matplotlib Demo in Streamlit")

# Sample data
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 12, 37]
data = np.random.randn(1000)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# 1️⃣ Line + Scatter plot
axs[0, 0].plot(x, y1, label='sin(x)', color='blue', linestyle='--', marker='o')
axs[0, 0].plot(x, y2, label='cos(x)', color='red', linestyle='-', marker='x')
axs[0, 0].set_title("Line Plot")
axs[0, 0].set_xlabel("X Axis")
axs[0, 0].set_ylabel("Y Axis")
axs[0, 0].legend()
axs[0, 0].grid(True)

# 2️⃣ Bar Chart
axs[0, 1].bar(categories, values, color='purple')
axs[0, 1].set_title("Bar Chart")
axs[0, 1].set_xlabel("Categories")
axs[0, 1].set_ylabel("Values")
for i, v in enumerate(values):
    axs[0, 1].text(i, v + 1, str(v), ha='center')

# 3️⃣ Histogram
axs[1, 0].hist(data, bins=20, color='orange', edgecolor='black')
axs[1, 0].set_title("Histogram")
axs[1, 0].set_xlabel("Value")
axs[1, 0].set_ylabel("Frequency")

# 4️⃣ Pie Chart
axs[1, 0].pie(values, labels=categories, autopct='%1.1f%%', startangle=90, shadow=True)
axs[1, 0].set_title("Pie Chart")

# Adjust layout
plt.tight_layout()

# Show in Streamlit
st.pyplot(fig)

# Option to save
with st.expander("💾 Save This Plot"):
    if st.button("Save as PNG"):
        fig.savefig("matplotlib_demo.png")
        st.success("Saved as matplotlib_demo.png")
