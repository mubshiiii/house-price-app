import streamlit as st

st.title("🏠 House Price Prediction System")

st.subheader("Enter Property Details")

area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
location = st.text_input("Location")
year_built = st.number_input("Year Built")

if st.button("Predict Price"):
    price = (area * 1500) + (bedrooms * 500000) + (bathrooms * 300000)

    st.success(f"Estimated Price: {price} PKR")
