import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

## Loading the trained model
model = tf.keras.models.load_model('model.keras')

## load the encoders and scaler
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)

with open('ohe.pkl','rb') as file:
    ohe_encoder = pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)
    
## streamlit app
st.title('Customer Churn Prediction')

# User input
geography = st.selectbox('Geography', ohe_encoder.categories_[0])  # accepts a 1D array or list
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

## prepare the input Data
input_data = pd.DataFrame({
    'Geography': [geography],
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],  ## gives an array, so [0] used 
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

## OHE and label encoding

df = input_data

ohe_columns = ohe_encoder.transform(df[['Geography']]).astype(int)
ohe_columns = pd.DataFrame(ohe_columns,columns=ohe_encoder.get_feature_names_out())
df = pd.concat([df,ohe_columns],axis=1)
df.drop(columns='Geography',inplace=True)


## scaling the data
df = scaler.transform(df)

    
## Predict churn
if st.button("Predict"):
    prediction = model.predict(df)
    prediction_prob = prediction[0][0]

    if prediction_prob > 0.5:
        st.write('The customer is likely to churn.')
    else:
        st.write('The customer is not likely to churn.')