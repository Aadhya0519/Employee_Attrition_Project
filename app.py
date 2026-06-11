import streamlit as st
import pandas as pd
import joblib

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="👨‍💼",
    layout="wide"
)

# -----------------------------------
# Load Model
# -----------------------------------
model = joblib.load("models/employee_attrition_final_model.joblib")

# -----------------------------------
# Sidebar Navigation
# -----------------------------------
st.sidebar.image(
    "https://img.icons8.com/color/96/businessman.png",
    width=80
)

st.sidebar.title("👨‍💼 Employee Attrition")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🤖 Predict Attrition",
        "📋 Feature Guide",
        "ℹ️ About Project"
    ]
)

# ===================================
# HOME PAGE
# ===================================
if page == "🏠 Home":

    st.title("👨‍💼 Employee Attrition Prediction System")

    st.markdown("""
    ### Welcome!

    This application predicts whether an employee is likely to:

    - ✅ **Stay with the company**
    - ⚠️ **Leave the company**

    The prediction is made using a **Random Forest Classifier** trained on employee information.

    Use the sidebar to navigate to the prediction page.
    """)

    st.info(
        "🎯 Goal: Help organizations identify employees at risk of attrition and support better retention strategies."
    )

# ===================================
# FEATURE GUIDE
# ===================================
elif page == "📋 Feature Guide":

    st.title("📋 Feature Guide")

    guide = pd.DataFrame({
        "Feature": [
            "Age",
            "Years at Company",
            "Monthly Income",
            "Work-Life Balance",
            "Number of Promotions",
            "Distance From Home",
            "Income Per Year",
            "Job Role",
            "Education Level",
            "Marital Status",
            "Number of Dependents",
            "Job Level",
            "Company Tenure",
            "Remote Work",
            "Promotion Rate"
        ],
        "Description": [
            "Employee age",
            "Years worked in company",
            "Monthly salary",
            "0 = Lowest, 3 = Highest",
            "Total promotions received",
            "Distance to office",
            "Annual salary",
            "Encoded value (0-4)",
            "Encoded value (0-4)",
            "Encoded value (0-2)",
            "Number of dependents",
            "Encoded value (0-2)",
            "Total tenure in company",
            "0 = No, 1 = Yes",
            "Promotion frequency"
        ]
    })

    st.dataframe(guide, use_container_width=True)

# ===================================
# ABOUT PAGE
# ===================================
elif page == "ℹ️ About Project":

    st.title("ℹ️ About This Project")

    st.markdown("""
### Project Name
Employee Attrition Prediction

### Final Model
✅ Random Forest Classifier

### Technologies Used
- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

### Workflow
- Data Preprocessing
- Feature Engineering
- Feature Selection
- Hyperparameter Tuning
- Final Model Building
- Streamlit Deployment

### Output
Predicts whether an employee is likely to:
- Stay
- Leave
""")

# ===================================
# PREDICTION PAGE
# ===================================
else:

    st.title("🤖 Predict Employee Attrition")

    st.write("Fill in the employee details below.")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30
        )

        years_at_company = st.number_input(
            "Years at Company",
            min_value=0,
            value=5
        )

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=0.0,
            value=5000.0
        )

        work_life_options = {
            "0 - Poor": 0,
            "1 - Fair": 1,
            "2 - Good": 2,
            "3 - Excellent": 3
        }

        selected_wlb = st.selectbox(
            "⚖️ Work-Life Balance",
            options=list(work_life_options.keys())
        )

        work_life_balance = work_life_options[selected_wlb]

        number_of_promotions = st.number_input(
            "Number of Promotions",
            min_value=0,
            value=0
        )

        distance_from_home = st.number_input(
            "Distance From Home",
            min_value=0,
            value=10
        )

        income_per_year = st.number_input(
            "Income Per Year",
            min_value=0.0,
            value=60000.0
        )

    with col2:

        job_role_options = {
            "0 - Education": 0,
            "1 - Media": 1,
            "2 - Healthcare": 2,
            "3 - Technology": 3,
            "4 - Finance": 4
        }

        selected_job_role = st.selectbox(
            "💼 Job Role",
            options=list(job_role_options.keys())
        )

        job_role = job_role_options[selected_job_role]

        education_options = {
        "0 - High School": 0,
        "1 - Associate Degree": 1,
        "2 - Bachelor’s Degree": 2,
        "3 - Master’s Degree": 3,
        "4 - PhD": 4
        }

        selected_education = st.selectbox(
            "🎓 Education Level",
            options=list(education_options.keys())
        )

        education_level = education_options[selected_education]

        marital_options = {
            "0 - Single": 0,
            "1 - Married": 1,
            "2 - Divorced": 2
        }

        selected_marital = st.selectbox(
            "💍 Marital Status",
            options=list(marital_options.keys())
        )

        marital_status = marital_options[selected_marital]

        number_of_dependents = st.number_input(
            "Number of Dependents",
            min_value=0,
            value=0
        )

        job_level_options = {
            "0 - Entry": 0,
            "1 - Mid": 1,
            "2 - Senior": 2
        }

        selected_job_level = st.selectbox(
            "🏢 Job Level",
            options=list(job_level_options.keys())
        )

        job_level = job_level_options[selected_job_level]

        company_tenure = st.number_input(
            "Company Tenure",
            min_value=0,
            value=5
        )

        remote_work = st.selectbox(
            "Remote Work",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes"
        )

        promotion_rate = st.number_input(
            "Promotion Rate",
            min_value=0.0,
            value=0.10
        )

    st.markdown("---")

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

        st.subheader("📄 Input Summary")
        st.dataframe(input_df, use_container_width=True)

        prediction = model.predict(input_df)

        st.markdown("---")
        st.subheader("📊 Prediction Result")

        if prediction[0] == 0:
            st.error(
                "⚠️ The model predicts that the employee is **likely to leave the company.**"
            )
        else:
            st.snow()
            st.success(
                "✅ The model predicts that the employee is **likely to stay with the company.**"
            )

        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(input_df)[0]
            leave_prob = probs[0] * 100
            stay_prob = probs[1] * 100

            st.markdown("### 📈 Prediction Confidence")
            st.progress(int(max(leave_prob, stay_prob)))

            c1, c2 = st.columns(2)
            c1.metric("Leave Probability", f"{leave_prob:.2f}%")
            c2.metric("Stay Probability", f"{stay_prob:.2f}%")

st.markdown("---")
st.caption(
    "🚀 Employee Attrition Prediction • Random Forest • Streamlit"
)