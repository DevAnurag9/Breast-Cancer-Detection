import streamlit as st
import pandas as pd
import joblib

model = joblib.load("breast_cancer_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Breast Cancer Predictor")

st.title("🩺 Breast Cancer Prediction")
st.write("Predict whether tumor is benign or malignant")

st.sidebar.header("Enter Top 5 Values")

radius = st.sidebar.text_input("Worst Radius", "17.9")
perimeter = st.sidebar.text_input("Worst Perimeter", "184.6")
concavity = st.sidebar.text_input("Worst Concavity", "0.71")
mean_radius = st.sidebar.text_input("Mean Radius", "17.9")
mean_area = st.sidebar.text_input("Mean Area", "1001")

if st.sidebar.button("Predict"):
    input_df = pd.DataFrame([[
        float(radius),
        float(perimeter),
        float(concavity),
        float(mean_radius),
        float(mean_area)
    ]], columns=[
        "worst radius",
        "worst perimeter",
        "worst concavity",
        "mean radius",
        "mean area"
    ])

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Malignant Tumor Detected")
    else:
        st.success("✅ Benign Tumor")
