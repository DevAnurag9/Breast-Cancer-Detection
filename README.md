# 🩺 Breast Cancer Detection using Machine Learning

## 📌 Overview

This project is a **Machine Learning-based Breast Cancer Detection System** that predicts whether a tumor is **Benign (Non-Cancerous)** or **Malignant (Cancerous)** using clinical features.

The model is trained on the **UCI Wisconsin Diagnostic Dataset** and deployed using **Streamlit** for real-time predictions.

---

## 🚀 Features

* Binary classification: **Benign vs Malignant**
* Achieved **98.24% accuracy using SVM**
* Top-5 feature optimization for faster prediction
* Real-time prediction using Streamlit web app
* Clean and reproducible ML pipeline

---

## 📂 Dataset

* **Source:** UCI Machine Learning Repository
* **Dataset:** Breast Cancer Wisconsin (Diagnostic)
* **Samples:** 569
* **Features:** 30 numerical features
* **Target:** Diagnosis (Benign = 0, Malignant = 1)

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Joblib
* Streamlit
* Google Colab
* GitHub
* Streamlit Cloud

---

## 🔄 Machine Learning Pipeline

```
UCI Dataset
   ↓
CSV Conversion
   ↓
Data Preprocessing
   ↓
Label Encoding
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training (LR, RF, SVM)
   ↓
Model Evaluation
   ↓
Top-5 Feature Selection
   ↓
Model Serialization (.pkl)
   ↓
Streamlit Deployment
```

---

## 🧠 Models Used

| Model               | Accuracy   |
| ------------------- | ---------- |
| Logistic Regression | 97.36%     |
| Random Forest       | 96.49%     |
| SVM                 | **98.24%** |

✅ **Final Model: Support Vector Machine (SVM)**

---

## 📊 Performance Metrics

* Accuracy
* Precision
* Recall ⭐ (Most important for healthcare)
* F1-score
* Confusion Matrix

---

## 🌐 Deployment

The model is deployed using **Streamlit Cloud**.

👉 Users can input 5 tumor-related features:

* Worst Radius
* Worst Perimeter
* Worst Concavity
* Mean Radius
* Mean Area

And get instant prediction:

* ✅ Benign
* ⚠️ Malignant

---

## ⚠️ Challenges Faced

* Feature mismatch between training and deployment
* Scaling inconsistency
* Streamlit deployment issues
* Tunnel-based testing limitations

---

## 🔮 Future Scope

* Add prediction probability (confidence score)
* Integrate SHAP for explainability
* Use deep learning models
* Mobile app deployment
* Real hospital dataset integration

---

## 👨‍💻 Authors

**Anurag Kumar Singh**

---

## 🎤 Viva Insight

> This project demonstrates how machine learning can assist in early cancer detection by combining high accuracy with real-time deployment.

---

## ⭐ Acknowledgment

Special thanks to:

* UCI Machine Learning Repository
* KIET Faculty (Ms. Kirti Sharma)
* Open-source ML community

---

## 📜 License

This project is for **educational and research purposes only**.
