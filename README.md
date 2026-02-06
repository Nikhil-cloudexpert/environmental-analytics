# Predicting Air Quality Index (AQI)

## Problem Overview
Air pollution monitoring is critical for public health and policy-making.  
This project builds an end-to-end machine learning solution to predict the Air Quality Index (AQI) using environmental and pollution-related data.

Since the raw dataset does not contain a directly computed AQI value, PM2.5 concentration is used as a proxy target, which is a commonly accepted approach in air quality analytics.

---

## Data Source
Environmental and air quality data collected from public sources related to Indian air pollution.  
The dataset includes pollutant concentrations, temporal information, and location-based attributes.

- Data type: Numerical and categorical  
- Size: 1000+ rows (recommended), multiple features  
- Target variable: PM2.5 (used as AQI proxy)

---

## Models Used
Multiple regression models were trained, evaluated, and compared, including:

- Linear Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  

The final model was selected based on performance metrics such as **R² Score** and **RMSE**.

---

## Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Streamlit  

---

## How to Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
