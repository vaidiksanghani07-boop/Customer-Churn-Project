import joblib
import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path

st.title("Customer Churn Prediction")

st.write("This application predicts whether a customer is likely to churn "
        "using a trained Random Forest model.")

model_path = Path(__file__).parent.parent / "models" / "random_forest.pkl"
model = joblib.load(model_path)

st.header("Enter Customer Information")

gender = st.selectbox("Gender", ["Male", "Female"])

senior_citizen = st.selectbox("Senior Citizen",["Yes", "No"])
partner = st.selectbox("Partner",["Yes", "No"])
dependents = st.selectbox("Dependents",["Yes", "No"])
tenure = st.number_input("Tenure (Months)",min_value=0,step=1)

phone_service = st.selectbox("Phone Service",["Yes", "No"])

internet_service = st.selectbox("Internet Service",["DSL", "Fiber optic", "No"])

contract = st.selectbox("Contract",["Month-to-month", "One year", "Two year"])

monthly_charges = st.number_input("Monthly Charges",min_value=0.0,value=50.0)

total_charges = st.number_input("Total Charges",min_value=0.0,value=50.0)



input_data = pd.DataFrame({
        "gender" : [gender] ,
        "SeniorCitizen": [senior_citizen],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "InternetService": [internet_service],
        "Contract": [contract],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
})

input_data = pd.get_dummies(input_data , drop_first = True)

input_data = input_data.reindex(columns = model.feature_names_in_, fill_value = 0)

if st.button("predict churn "):
        prediction = model.predict(input_data)

        if prediction[0] == 1:
                st.error("Customer is likely to churn.")
        else:
                st.success("customer is unlikely to churn.")
        


        