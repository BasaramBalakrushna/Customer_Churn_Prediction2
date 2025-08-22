import streamlit as st
import pandas as pd
import joblib



# # Load the model from the same folder as app.py
# model = joblib.load("rf_model_compressed.pkl")
# print("✅ Model loaded successfully!")


# import os
# import joblib
# import streamlit as st

# model_path = "rf_model_compressed.pkl"

# # Check if model exists
# if not os.path.exists(model_path):
#     st.error(f"❌ Model file not found: {model_path}. Please make sure it is in the same folder as app.py.")
#     st.stop()

# # Load the model
# model = joblib.load(model_path)
# st.success("✅ Model loaded successfully!")


import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), "rf_model_compressed.pkl")
model = joblib.load(model_path)
print("✅ Model loaded successfully!")












st.title("Customer Churn Predictor App")
st.markdown("Fill Up The Customer Details To Predict The Churn")
# Feature 1: Total Number Of Orders
total_orders = st.number_input("Total Orders (Minimum 1)",min_value=1,value=3)
# Feature 2: Total Spend By Customers
total_spend = st.number_input('Total Spend',min_value=10,value=100,step=10)
# Feature 3: Average Spend Per Order
avg_spent = st.number_input('Average Spent Per Order',min_value=10,value=100,step=10)
# Feature 4: Average Review Score
avg_review_score = st.slider('Average Review Score',min_value=1.0,max_value=5.0,value=2.76)
# Feature 5: Number Of Payment Methods
num_payments_methods = st.radio('Number Of Payment Methods',options=[1,2,3])
num_tenure_days = st.number_input('Number Of Tenure Days',min_value=0,value=15,step=30)

input_data = pd.DataFrame({
    'total_orders': [total_orders],
    'total_spend': [total_spend],
    'avg_spend_per_order': [avg_spent],
    'avg_review_score': [avg_review_score],
    'num_payment_methods': [num_payments_methods],
    'customer_tenure_days': [num_tenure_days]
})

if st.button('Predict Churn'):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"The Customer Is Going To Churn With The Confidence Percentage of {probability}.")
    else:
        st.success(f"The Customer Is Not Going To Churn With The Confidence Percentage of {probability}.")