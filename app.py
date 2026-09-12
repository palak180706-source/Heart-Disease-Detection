import streamlit as st
import pandas as pd
import joblib

model=joblib.load('KNN_heart.pkl')
scaler=joblib.load('scaler.pkl')
expected_columns=joblib.load('columns.pkl')


st.title("Heart stroke Prediction App by palak")
st.markdown("provide the following details")

age=st.slider("Age", 18, 100, 40)
sex=st.selectbox("Sex", ["Male", "Female"])
chestpain=st.selectbox("Chest Pain Type",["ATA","NAP","ASY","TA"])
restbps=st.number_input("Resting Blood Pressure(mmHg)", 80, 200, 120)
cholestrol=st.number_input("Cholesterol(mg/dl)", 100, 600, 200)
fastingbs=st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
restingecg=st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr=st.slider("Max Heart Rate", 60, 220, 150)
excercise_angina=st.selectbox("Exercise Induced Angina", ["Y", "N"])   
oldpeak=st.slider("Old Peak", 0.0, 6.0, 1.0)
st_slope=st.selectbox("ST Slope", ["Up", "Flat", "Down"])


if st.button("Predict"):
    raw_data = {
        
        "age": age,
        "sex" + sex: 1,
        "chestpain" +chestpain:1,
        "restbps": restbps,
        "cholestrol": cholestrol,
        "fastingbs": fastingbs,
        "restingecg" + restingecg:1,
        "max_hr": max_hr,
        "excercise_angina" + excercise_angina:1,
        "oldpeak": oldpeak,
        "st_slope" + st_slope:1
    }

    input_data = pd.DataFrame([raw_data])

    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[expected_columns]

    scaled_input_data = scaler.transform(input_data)
    prediction = model.predict(scaled_input_data)[0]

    if prediction == 1:
        st.error("The patient is likely to have a heart stroke.")
    else:
        st.success("The patient is unlikely to have a heart stroke.")


