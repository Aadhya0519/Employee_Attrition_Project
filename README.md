# Employee Attrition Prediction System

## Project Overview

This project predicts whether an employee is likely to leave the company using Machine Learning techniques. The goal is to help organizations identify employees who may be at risk of attrition and support data-driven retention strategies.

---

## Machine Learning Model

After comparing multiple classification algorithms, the **Random Forest Classifier** was selected as the final model because it achieved the best overall performance based on evaluation metrics such as Accuracy, Precision, Recall, and F1-Score.

Models evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Naive Bayes

---

## Project Features

* Employee attrition prediction using Machine Learning
* Data preprocessing and feature engineering
* Model comparison and evaluation
* Hyperparameter tuning for model optimization
* Model serialization using Joblib
* Interactive web application built with Streamlit
* GitHub project structure for version control

---

## Project Structure

```
Employee_Attrition_Project/
│
├── data/
├── models/
├── notebooks/
├── src/
├── app.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser and allow you to enter employee details to generate an attrition prediction.

---

## Model Output

The application predicts one of the following outcomes:

* **Employee is likely to stay with the company**
* **Employee is likely to leave the company**

---

## Future Enhancements

* Add user-friendly categorical dropdown menus
* Deploy the application to a cloud platform
* Include probability scores along with predictions
* Add model monitoring and logging capabilities
