# Customer Churn Prediction

## Project Overview

This project predicts whether a customer is likely to churn using Machine Learning classification models.

The goal is to identify customers who are likely to leave the service so that businesses can take preventive actions.

## Dataset

The project uses the Telco Customer Churn dataset.

The dataset contains customer information such as:

- Customer demographics
- Tenure
- Services
- Contract details
- Monthly charges
- Total charges
- Churn status

## Project Workflow

The project follows these steps:

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Hyperparameter Tuning
8. Model Comparison
9. Final Model Selection
10. Streamlit Deployment

## Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary columns
- Handled categorical features using One-Hot Encoding
- Used `drop_first=True` to avoid redundant dummy variables
- Split the data into training and testing sets
- Used stratified splitting to maintain the class distribution
- Applied StandardScaler for Logistic Regression

## Models Used

The following classification models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

## Model Comparison

| Model |           |Accuracy | Precision | Recall |F1 Score|
|Logistic Regression| 78.14%  | 60.12%    | 52.41% | 56.00% |
| Decision Tree     | 78.64%  | 68.16%    | 36.63% | 47.65% |
| Random Forest     | 68.70%  | 45.01%    | 80.75% | 57.80% |
| XGBoost           | 79.99%  | 66.20%    | 50.27% | 57.14% |

## Final Model Selection

Random Forest was selected as the final model.

Although XGBoost achieved the highest accuracy, customer churn prediction focuses on identifying as many potential churn customers as possible.

Random Forest achieved:

- Recall: **80.75%**
- F1 Score: 57.80%

It achieved the highest Recall and F1 Score among the evaluated models.

Therefore, Random Forest was selected as the final model based on the project's focus on detecting potential churn customers.

## Streamlit Application

A Streamlit web application was created to allow users to enter customer information and receive a churn prediction.

The application provides two possible outputs:

- Customer is likely to churn
- Customer is unlikely to churn

## Project Structure

Customer_Churn_Project/

├── data/

├── notebooks/

├── models/

├── app/

│   └── app.py

├── reports/

├── requirements.txt

└── README.md