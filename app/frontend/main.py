import streamlit as st
import requests
import os
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get the API URL from environment variable
API_URL = os.getenv('PREDICT_FLOWER_SPECIES_URL')

# Streamlit UI
st.title("Flower Species Prediction")

# Input fields for flower features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0)

# Button to make prediction
if st.button("Predict"):
    # Prepare the input data
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    
    # Call the prediction endpoint
    response = requests.post(API_URL, json=input_data, timeout=5)
    
    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Predicted Flower Species: {prediction['species']}")
    else:
        logging.error(f"Error: {response.status_code}")
        st.error("Error in prediction. Please try again.")
