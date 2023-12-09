import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('Churnpickle', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app
st.title('Credit Scoring Prediction')

# Sidebar with user input
st.sidebar.header('User Input Features')

# Create a dictionary to store user input
user_input = {}

# Add input fields to the sidebar
user_input['CreditScore'] = st.sidebar.slider('Credit Score', min_value=300, max_value=850, value=700)
user_input['Age'] = st.sidebar.slider('Age', min_value=18, max_value=100, value=30)
user_input['Tenure'] = st.sidebar.slider('Tenure', min_value=0, max_value=10, value=5)
user_input['Balance'] = st.sidebar.number_input('Balance', min_value=0.0, value=0.0)
user_input['NumOfProducts'] = st.sidebar.slider('Number of Products', min_value=1, max_value=4, value=1)
user_input['HasCrCard'] = st.sidebar.selectbox('Has Credit Card', [0, 1])
user_input['IsActiveMember'] = st.sidebar.selectbox('Is Active Member', [0, 1])
user_input['EstimatedSalary'] = st.sidebar.number_input('Estimated Salary', min_value=0.0, value=50000.0)
user_input['Male'] = st.sidebar.selectbox('Gender (Male=1, Female=0)', [0, 1])
user_input['Country_val'] = st.sidebar.selectbox('Country', ['Country1', 'Country2', 'Country3'])  # Replace with actual country names

# Create a DataFrame from user input
user_data = pd.DataFrame([user_input])

# Display the user input data
st.subheader('User Input:')
st.write(user_data)

# Make predictions using the loaded model
if st.button('Predict'):
    prediction = model.predict(user_data)
    st.subheader('Prediction:')
    st.write(prediction)
