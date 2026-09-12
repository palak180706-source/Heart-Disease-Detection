# ❤️ Heart Stroke Prediction App

A Machine Learning based web application that predicts the likelihood of heart stroke using patient health-related parameters.

The application is built using Python, Scikit-learn and Streamlit. It provides a simple and interactive interface where users can enter health information and get a prediction instantly.

## 🚀 Live Demo

🔗 **Live App:**  
https://heart-disease-detection-9b4r9vpsfyu6vf5p33labx.streamlit.app/

## 📌 Project Overview

Heart stroke is a serious health condition that can be influenced by several factors such as age, blood pressure, glucose level, BMI, smoking habits and other health parameters.

This project uses a trained **K-Nearest Neighbors (KNN)** machine learning model to predict whether a person is at risk of heart stroke based on the given input features.

> **Note:** This application is developed for educational and demonstration purposes only. It is not a medical diagnostic tool.

## 🎯 Objectives

- Predict the possibility of heart stroke using Machine Learning.
- Provide a simple and user-friendly web interface.
- Allow users to enter patient health information easily.
- Generate predictions quickly using a trained ML model.
- Demonstrate the practical implementation of Machine Learning with Streamlit.

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
- **Git & GitHub**

## 🤖 Machine Learning Model

The project uses a **K-Nearest Neighbors (KNN)** classification algorithm.

### Model Workflow

1. Collect patient health-related data.
2. Perform data preprocessing.
3. Scale the input features.
4. Train the KNN classification model.
5. Save the trained model using Joblib.
6. Load the model into the Streamlit application.
7. Take user inputs.
8. Apply the same preprocessing/scaling.
9. Generate the final prediction.

## 📊 Input Features

The application uses health-related parameters such as:

- Age
- Gender
- Hypertension
- Heart Disease
- Average Glucose Level
- BMI
- Smoking Status
- Other relevant patient parameters

The exact input fields available in the application may depend on the trained dataset and model.

## 📁 Project Structure

```text
heart-disease-detection/
│
├── app.py
├── KNN_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
