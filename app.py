import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="House Price Prediction", layout="centered")

# ⭐ PROFILE BOX
st.markdown("""
<div style="
position: fixed;
top: 10px;
right: 20px;
background-color: white;
padding: 10px 14px;
border-radius: 12px;
box-shadow: 0px 0px 12px rgba(0,0,0,0.2);
z-index: 9999;
text-align:center;
">
👤 <b>Mubshir Nadeem</b><br>
🔗 <a href="https://your-link.com" target="_blank">View Profile</a>
</div>
""", unsafe_allow_html=True)

# TITLE
st.title("🏠 Pakistan House Price Prediction AI")
st.markdown("Fill all details below to estimate house price")

# ---------------- CITY DROPDOWN ----------------
city = st.selectbox("Select City", [
    "Lahore",
    "Karachi",
    "Islamabad",
    "Faisalabad",
    "Sargodha"
])

# ---------------- AREAS DATA ----------------
city_areas = {
    "Lahore": [
        "DHA", "Bahria Town", "Gulberg", "Johar Town",
        "Model Town", "Cantt", "Allama Iqbal Town"
    ],
    "Karachi": [
        "DHA", "Clifton", "Gulshan-e-Iqbal", "Malir",
        "North Nazimabad", "Korangi"
    ],
    "Islamabad": [
        "F-6", "F-7", "F-10", "G-11",
        "Bahria Town", "DHA Islamabad"
    ],
    "Faisalabad": [
        "Madina Town", "People's Colony", "Ghulam Muhammadabad",
        "Jaranwala Road", "Samanabad"
    ],
    "Sargodha": [
        "Satellite Town", "Cantt Area", "University Road",
        "City Center"
    ]
}

# ---------------- AREA DROPDOWN ----------------
area = st.selectbox("Select Area", city_areas[city])

# ---------------- INPUTS ----------------
area_size = st.number_input("Area (Square Feet)", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10)
floors = st.number_input("Floors", min_value=1, max_value=5)
age = st.number_input("House Age (Years)", min_value=0)

# ---------------- PREDICTION ----------------
if st.button("Predict Price"):

    price = (
        (area_size * 1200) +
        (bedrooms * 500000) +
        (bathrooms * 300000) +
        (floors * 200000)
    )

    st.success(f"Estimated Price: {round(price, 2)} PKR")

    st.info(f"Location: {city} → {area}")
    st.info("Note: This is demo model (real ML model can be connected next step)")
