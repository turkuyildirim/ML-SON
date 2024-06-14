import pandas as pd
import streamlit as st
import pickle
import numpy as np


# Load the trained model
with open("best_model.pkl", 'rb') as model_file:
    best_model = pickle.load(model_file)
    
  

def main():
    
    #giving a title
    st.title('Bank Term Deposit Subscription Prediction')
    
    st.write("This app predicts whether a customer will subscribe to a term deposit based on their features.")
    
    #getting input from the user
    age = st.number_input("Age", min_value=0, max_value=100, value=30)
    job = st.selectbox("Job", ["admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown"])
    marital = st.selectbox("Marital Status", ["divorced", "married", "single", "unknown"])
    education = st.selectbox("Education", ["basic.4y", "basic.6y", "basic.9y", "high.school", "illiterate", "professional.course", "university.degree", "unknown"])
    default = st.selectbox("Default", ["no", "yes", "unknown"])
    housing = st.selectbox("Housing", ["no", "yes", "unknown"])
    loan = st.selectbox("Loan", ["no", "yes", "unknown"])
    contact = st.selectbox("Contact", ["cellular", "telephone"])
    month = st.selectbox("Month", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
    day_of_week = st.selectbox("Day of Week", ["mon", "tue", "wed", "thu", "fri"])
    campaign = st.number_input("Campaign", min_value=0, max_value=100, value=1)
    previous = st.number_input("Previous", min_value=0, max_value=100, value=0)
    poutcome = st.selectbox("Poutcome", ["failure", "nonexistent", "success"])
    emp_var_rate = st.number_input("Emp Var Rate", value=1.0)
    cons_price_idx = st.number_input("Cons Price Index", value=1.0)
    cons_conf_idx = st.number_input("Cons Confidence Index", value=-40.0)
    euribor3m = st.number_input("Euribor 3 Month Rate", value=1.0)
    nr_employed = st.number_input("Number of Employees", value=5000)
        
        
    user_data = pd.DataFrame({
            'age': [age],
            'job': [job],
            'marital': [marital],
            'education': [education],
            'default': [default],
            'housing': [housing],
            'loan': [loan],
            'contact': [contact],
            'month': [month],
            'day_of_week': [day_of_week],
            'campaign': [campaign],
            'previous': [previous],
            'poutcome': [poutcome],
            'emp.var.rate': [emp_var_rate],
            'cons.price.idx': [cons_price_idx],
            'cons.conf.idx': [cons_conf_idx],
            'euribor3m': [euribor3m],
            'nr.employed': [nr_employed]
    })
        
   

    # Display prediction
    if st.button('Predict'):
        result = predict()
        st.write(f"The client will subscribe a term deposit: {result}")
        
    

if __name__ == '__main__':
    main()
