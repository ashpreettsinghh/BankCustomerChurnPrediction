import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('Churnpickle', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to convert country name to numeric value
def country(cname):
    if cname == 'France':
        return 1
    elif cname == 'Germany':
        return 2
    elif cname == 'Spain':
        return 3

# Streamlit app
st.title('Bank Customer Churn Prediction')

# Sidebar with user input
st.sidebar.header('User Input(s)')

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

# Add a selectbox for country with the converted numeric values
user_input['Country_val'] = country(st.sidebar.selectbox('Country', ['France', 'Germany', 'Spain']))

# Create a DataFrame from user input
user_data = pd.DataFrame([user_input])

# Display the user input data
st.subheader('User Input:')
st.write(user_data)

# Make predictions using the loaded model
if st.button('Predict'):
    prediction = model.predict(user_data)
    st.subheader('Prediction:')
    
    # Display whether the customer has exited the bank or not
    if prediction == 0:
        st.write('The customer is predicted to **NOT** have exited the bank.')
    else:
        st.write('The customer is predicted to have exited the bank.')
