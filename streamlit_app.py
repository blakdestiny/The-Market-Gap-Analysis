import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("snacks_clean.csv")

st.title("Sugar Trap: Snack Market Gap Analysis")

categories = st.multiselect(
    "Filter by category",
    options=df["primary_category"].unique(),
    default=df["primary_category"].unique(),
)
filtered = df[df["primary_category"].isin(categories)]

fig = px.scatter(filtered, x="sugars_100g", y="proteins_100g", color="primary_category", opacity=0.6)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Key Insight")
st.info("Based on the data, the biggest market opportunity is in Chocolate/Candy, "
        "specifically targeting products with 10g of protein and less than 8g of sugar.")
