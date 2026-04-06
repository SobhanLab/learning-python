import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction (BD)")

st.write("Enter house details:")

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
area = st.number_input("Area (sqft)", min_value=500, max_value=10000, value=1500)

if st.button("Predict Price"):
    data = np.array([[bedrooms, bathrooms, area]])
    
    prediction = model.predict(data)
    
    st.success(f"Estimated Price: {prediction[0]:,.0f} BDT")
