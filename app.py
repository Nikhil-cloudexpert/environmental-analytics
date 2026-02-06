import streamlit as st
import pickle
import numpy as np

# Load model and feature metadata
model = pickle.load(open("models/best_model.pkl", "rb"))
feature_columns = pickle.load(open("models/feature_columns.pkl", "rb"))

st.set_page_config(page_title="AQI Prediction", layout="centered")

st.title("🌫️ Air Quality Index (AQI) Prediction")
st.write("Enter environmental parameters to predict AQI")

# Collect inputs dynamically
user_inputs = []

for feature in feature_columns:
    value = st.number_input(f"{feature}", value=0.0)
    user_inputs.append(value)

if st.button("Predict AQI"):
    input_array = np.array([user_inputs])
    prediction = model.predict(input_array)
    st.success(f"✅ Predicted AQI: {prediction[0]:.2f}")
