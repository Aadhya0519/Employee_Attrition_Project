import joblib
import pandas as pd

model = joblib.load("models/employee_attrition_final_model.joblib")

def predict_employee(input_dict):
    df = pd.DataFrame([input_dict])
    return model.predict(df)