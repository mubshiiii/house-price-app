import streamlit as st

st.title("House Price Prediction - Mubshir")

area = st.number_input("Enter Area (sq ft)")
bedrooms = st.number_input("Bedrooms")

if st.button("Predict"):
    price = area * 2000 + bedrooms * 500000
    st.success(f"Estimated Price: {price} PKR")