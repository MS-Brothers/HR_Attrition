# 📊 HR Employee Attrition Prediction System

A Machine Learning project that predicts whether an employee is likely to leave the company based on HR-related features.  

This project uses **K-Nearest Neighbors (KNN)** with proper preprocessing and is deployed using **Streamlit**.

---

## 🚀 Project Overview

Employee attrition is a major concern for organizations.  
This project helps HR departments predict attrition risk using employee data such as:

- Age
- Monthly Income
- Distance From Home
- Job Satisfaction
- Work Life Balance
- Years At Company
- Overtime
- Marital Status
- Business Travel

The model predicts:
- 🟢 Employee will Stay
- 🔴 Employee will Leave

---

## 🧠 Machine Learning Approach

### 🔹 Data Preprocessing
- Handled categorical features using `pd.get_dummies()`
- Feature scaling applied
- Train-test split performed
- SMOTE used to handle class imbalance (if applicable)

### 🔹 Model Used
- **K-Nearest Neighbors (KNN)**
- Hyperparameter tuning using GridSearchCV
- Model saved using Pickle

---

## 📂 Project Structure
