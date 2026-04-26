import streamlit as st
import numpy as np

st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title("🏠 Pakistan House Price Prediction AI")

st.markdown("Fill all details below to estimate house price")

# Inputs
area = st.number_input("Area (Square Feet)", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10)
floors = st.number_input("Floors", min_value=1, max_value=5)
age = st.number_input("House Age (Years)", min_value=0)
location = st.selectbox("Location Type", ["Urban", "Suburban", "Rural"])

# Simple encoding
location_factor = {
    "Urban": 1.5,
    "Suburban": 1.2,
    "Rural": 1.0
}

# Prediction button
if st.button("Predict Price"):

    # Dummy ML formula (replace with real model later)
    price = (
        (area * 1200) +
        (bedrooms * 500000) +
        (bathrooms * 300000) +
        (floors * 200000)
    ) * location_factor[location]

    st.success(f"Estimated Price: {round(price, 2)} PKR")

    st.info("Note: This is AI demo model. You can connect real ML model later.")
