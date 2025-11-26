
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Streamlit application title
st.title('Employee Attrition Prediction App')

# Introduction and purpose of the application
st.markdown("""
This application predicts the likelihood of employee attrition based on various input features.
It utilizes a trained XGBoost model and applies the same preprocessing steps used during training.
""")

st.write("Streamlit app.py file generated successfully.")
