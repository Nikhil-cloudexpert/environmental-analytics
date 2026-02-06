import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("models/best_model.pkl", "rb"))

st.title("🌫️ AQI Prediction App")

st.write("Enter environmental parameters to predict AQI")

so2 = st.number_input("SO2")
no2 = st.number_input("NO2")
rspm = st.number_input("RSPM")
month = st.number_input("Month", min_value=1, max_value=12)
year = st.number_input("Year", min_value=1990, max_value=2030)

if st.button("Predict AQI"):
    features = np.array([[so2, no2, rspm, month, year]])
    prediction = model.predict(features)
    st.success(f"Predicted AQI: {prediction[0]:.2f}")
