import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="👨‍💼",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("models/employee_attrition_final_model.joblib")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📌 Project Information")
st.sidebar.write("""
**Project:** Employee Attrition Prediction

**Final Model:** Random Forest Classifier

This application predicts whether an employee is likely to leave the company based on selected employee attributes.
""")

# -------------------------------
# Main Title
# -------------------------------
st.title("👨‍💼 Employee Attrition Prediction System")
st.markdown(
    "Fill in the employee details below and click **Predict** to estimate whether the employee is likely to stay or leave."
)

st.divider()

# -------------------------------
# Input Layout
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    years_at_company = st.number_input("Years at Company", min_value=0, value=5)
    monthly_income = st.number_input("Monthly Income", min_value=0.0, value=5000.0)
    work_life_balance = st.slider("Work-Life Balance (0–3)", 0, 3, 2)
    number_of_promotions = st.number_input("Number of Promotions", min_value=0, value=0)
    distance_from_home = st.number_input("Distance From Home", min_value=0, value=10)
    income_per_year = st.number_input("Income Per Year", min_value=0.0, value=60000.0)

with col2:
    job_role = st.selectbox("Job Role (Encoded)", [0, 1, 2, 3, 4])
    education_level = st.selectbox("Education Level (Encoded)", [0, 1, 2, 3, 4])
    marital_status = st.selectbox("Marital Status (Encoded)", [0, 1, 2])
    number_of_dependents = st.number_input("Number of Dependents", min_value=0, value=0)
    job_level = st.selectbox("Job Level (Encoded)", [0, 1, 2])
    company_tenure = st.number_input("Company Tenure", min_value=0, value=5)
    remote_work = st.selectbox("Remote Work", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    promotion_rate = st.number_input("Promotion Rate", min_value=0.0, value=0.10)

st.divider()

# -------------------------------
# Prediction
# -------------------------------
if st.button("🚀 Predict Attrition", use_container_width=True):

    input_df = pd.DataFrame({
        "age": [age],
        "years_at_company": [years_at_company],
        "job_role": [job_role],
        "monthly_income": [monthly_income],
        "work-life_balance": [work_life_balance],
        "number_of_promotions": [number_of_promotions],
        "distance_from_home": [distance_from_home],
        "education_level": [education_level],
        "marital_status": [marital_status],
        "number_of_dependents": [number_of_dependents],
        "job_level": [job_level],
        "company_tenure": [company_tenure],
        "remote_work_Yes": [remote_work],
        "promotion_rate": [promotion_rate],
        "income_per_year": [income_per_year]
    })

    prediction = model.predict(input_df)

    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ The model predicts that the employee is **likely to leave the company**.")
    else:
        st.success("✅ The model predicts that the employee is **likely to stay with the company**.")

st.divider()

st.caption(
    "Machine Learning Project • Final Model: Random Forest Classifier • Built with Streamlit"
)