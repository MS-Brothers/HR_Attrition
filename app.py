# import streamlit as st
# import numpy as np
# import pandas as pd
# import pickle

# # Load trained model
# with open("attrition_model.pkl", "rb") as f:
#     model = pickle.load(f)

# st.set_page_config(page_title="HR Attrition Predictor", page_icon="📊")

# st.title("📊 HR Employee Attrition Prediction System")
# st.write("Provide employee details to predict whether the employee is likely to leave the company.")

# st.markdown("---")

# # ========== INPUT FIELDS ==========

# age = st.number_input("Age", min_value=18, max_value=60)

# monthly_income = st.number_input("Monthly Income", min_value=1000)

# distance_from_home = st.number_input("Distance From Home (KM)", min_value=0)

# job_satisfaction = st.slider("Job Satisfaction Level", 1, 4)

# work_life_balance = st.slider("Work Life Balance", 1, 4)

# years_at_company = st.number_input("Years At Company", min_value=0)

# overtime = st.selectbox("OverTime", 
#                         options=[0, 1], 
#                         format_func=lambda x: "No" if x == 0 else "Yes")

# marital_status = st.selectbox("Marital Status", 
#                               options=[0, 1], 
#                               format_func=lambda x: "Married" if x == 0 else "Single")

# business_travel = st.selectbox("Business Travel Frequently", 
#                                options=[0, 1], 
#                                format_func=lambda x: "No" if x == 0 else "Yes")

# st.markdown("---")

# # ========== PREDICTION BUTTON ==========

# if st.button("Predict Attrition"):

#     input_data = pd.DataFrame([[ 
#         age,
#         monthly_income,
#         distance_from_home,
#         job_satisfaction,
#         work_life_balance,
#         years_at_company,
#         overtime,
#         marital_status,
#         business_travel
#     ]], columns=[
#         'Age',
#         'MonthlyIncome',
#         'DistanceFromHome',
#         'JobSatisfaction',
#         'WorkLifeBalance',
#         'YearsAtCompany',
#         'OverTime_Yes',
#         'MaritalStatus_Single',
#         'BusinessTravel_Travel_Frequently'
#     ])

#     prediction = model.predict(input_data)[0]

#     st.subheader("Prediction Result")

#     if prediction == 1:
#         st.error("🔴 Employee is likely to LEAVE (Attrition = Yes)")
#     else:
#         st.success("🟢 Employee is likely to STAY (Attrition = No)")




import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("attrition_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load training columns
with open("train_columns.pkl", "rb") as f:
    train_columns = pickle.load(f)

st.set_page_config(page_title="HR Attrition Predictor", page_icon="📊")

st.title("📊 HR Employee Attrition Prediction System")
st.write("Provide employee details to predict whether the employee is likely to leave the company.")

st.markdown("---")

# ========== INPUT FIELDS ==========

age = st.number_input("Age", 18, 60)
monthly_income = st.number_input("Monthly Income", min_value=1000)
distance_from_home = st.number_input("Distance From Home (KM)", min_value=0)
job_satisfaction = st.slider("Job Satisfaction Level", 1, 4)
work_life_balance = st.slider("Work Life Balance", 1, 4)
years_at_company = st.number_input("Years At Company", min_value=0)

overtime = st.selectbox("OverTime", ["No", "Yes"])
marital_status = st.selectbox("Marital Status", ["Married", "Single"])
business_travel = st.selectbox("Business Travel", ["No", "Yes"])

st.markdown("---")

if st.button("Predict Attrition"):

    # Create base dataframe
    input_data = pd.DataFrame({
        'Age': [age],
        'MonthlyIncome': [monthly_income],
        'DistanceFromHome': [distance_from_home],
        'JobSatisfaction': [job_satisfaction],
        'WorkLifeBalance': [work_life_balance],
        'YearsAtCompany': [years_at_company],
        'OverTime': [overtime],
        'MaritalStatus': [marital_status],
        'BusinessTravel': [business_travel]
    })

    # Apply get_dummies same as training
    input_data = pd.get_dummies(input_data)

    # Match training columns (VERY IMPORTANT)
    input_data = input_data.reindex(columns=train_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🔴 Employee is likely to LEAVE (Attrition = Yes)")
    else:
        st.success("🟢 Employee is likely to STAY (Attrition = No)")