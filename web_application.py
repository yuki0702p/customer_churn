import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the model
@st.cache_resource
def load_model():
    return pickle.load(open('finalized_model.sav', 'rb'))

model = load_model()

# Define the updated transformers for the reduced input features
transforming = ColumnTransformer(transformers=[
    ('t1', StandardScaler(), ['age', 'cons_conf_idx', 'euribor3m', 'nr_employed']),
    ('t2', OneHotEncoder(), ['job', 'marital', 'housing', 'loan', 'contact', 'poutcome'])
], remainder='passthrough')

# Streamlit app
st.title('Customer Churn Prediction')

# Input fields
age = st.number_input('Age', min_value=18, max_value=100)
job = st.selectbox('Job', ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'])
marital = st.selectbox('Marital Status', ['divorced', 'married', 'single'])
housing = st.selectbox('Has housing loan?', ['no', 'yes'])
loan = st.selectbox('Has personal loan?', ['no', 'yes'])
contact = st.selectbox('Contact communication type', ['cellular', 'telephone'])
poutcome = st.selectbox('Outcome of the previous marketing campaign', ['failure', 'nonexistent', 'success'])
cons_conf_idx = st.number_input('Consumer confidence index', min_value=-50.0, max_value=50.0)
euribor3m = st.number_input('Euribor 3-month rate', min_value=0.0, max_value=10.0)
nr_employed = st.number_input('Number of employees', min_value=1000.0, max_value=6000.0)

# Prediction button
if st.button('Predict Churn'):
    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'age': [age], 
        'job': [job], 
        'marital': [marital], 
        'housing': [housing], 
        'loan': [loan], 
        'contact': [contact], 
        'poutcome': [poutcome], 
        'cons_conf_idx': [cons_conf_idx], 
        'euribor3m': [euribor3m], 
        'nr_employed': [nr_employed]
    })

    # Transform the input data
    transformed_data = transforming.fit_transform(input_data)

    # Make prediction
    prediction = model.predict(transformed_data)

    # Display result
    if prediction[0] == 'yes':
        st.error('This customer is likely to churn.')
    else:
        st.success('This customer is likely to stay.')
