import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu

heart_disease_model = pickle.load(open('./heart_disease_model.sav','rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           [#'Diabetes Prediction',
                            'Heart Disease Prediction'],
                            #'Parkinsons Prediction'],
                           
                           icons = ['activity','heart'],
                                    #,'person'],
                           
                           default_index = 0)
    
# st.write("""
# # Heart disease Prediction App

# This app predicts If a patient has a heart disease
# """)

# st.sidebar.header('User Input Features')

if(selected == 'Heart Disease Prediction'):
    
    #Page title
    st.title('Heart Disease Prediction using ML')
    
    age = st.number_input('Enter your age: (in years) ', key = 'age')

    sex  = st.selectbox('Sex: (1 = male; 0 = female)',(0,1),key='Sex')
    cp = st.selectbox('Chest pain type : (0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic)',(0,1,2,3), key = 'cp')
    trestbps = st.number_input('Resting blood pressure: (in mm Hg on admission to hospital) ' , key = 'tres')
    chol = st.number_input('Serum cholestrol in mg/dl: ', key = 'chol')
    fbs = st.selectbox('Fasting blood sugar > 120mg/dl :(1 = true, 0 = false)',(0,1), key = 'fbs')
    restecg = st.selectbox('Resting electrocardiographic results: (0 = normal, 1 = ST-T wave normality, 2 = left ventricular hypertrophy) ',(0,1,2),key = 'res')
    thalach = st.number_input('Maximum heart rate achieved: ',key = 'tha')
    exang = st.selectbox('Exercise induced angina: (1 = true, 0 = false) ',(0,1), key = 'exa')
    oldpeak = st.number_input('oldpeak ', key = 'old')
    slope = st.number_input('slope of the peak exercise ST segment: ', key = 'slope')
    ca = st.selectbox('number of major vessels : (0-3) colored by fluroscopy',(0,1,2,3), key = 'ca')
    thal = st.selectbox('thal : (thalium stress test result)',(0,1,2), key = 'thal')
    
    
    #Code for prediction
    heart_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person is suffering from Heart disease'
            
        else:
            heart_diagnosis = 'The person is Not suffering from Heart disease'
            
            
    st.success(heart_diagnosis)

# input_df = None
# # Collects user input features into dataframe


# age = st.sidebar.number_input('Enter your age: ', key = 'age')

# sex  = st.sidebar.selectbox('Sex',(0,1),key='Sex')
# cp = st.sidebar.selectbox('Chest pain type',(0,1,2,3), key = 'cp')
# trestbps = st.sidebar.number_input('Resting blood pressure: ' , key = 'tres')
# chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ', key = 'chol')
# fbs = st.sidebar.selectbox('Fasting blood sugar',(0,1), key = 'fbs')
# restecg = st.sidebar.number_input('Resting electrocardiographic results: ',key = 'res')
# thalach = st.sidebar.number_input('Maximum heart rate achieved: ',key = 'tha')
# exang = st.sidebar.selectbox('Exercise induced angina: ',(0,1), key = 'exa')
# oldpeak = st.sidebar.number_input('oldpeak ', key = 'old')
# slope = st.sidebar.number_input('he slope of the peak exercise ST segmen: ', key = 'slope')
# ca = st.sidebar.selectbox('number of major vessels',(0,1,2,3), key = 'ca')
# thal = st.sidebar.selectbox('thal',(0,1,2), key = 'thal')

    
# def make_prediction():

#         #Code for prediction
#     heart_diagnosis = ''
    
#     #Creating a button for prediction    
#     heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
#     if (heart_prediction[0]==1):
#         heart_diagnosis = 'The person is suffering from Heart disease'
            
#     else:
#         heart_diagnosis = 'The person is Not suffering from Heart disease'
            
            
#     st.success(heart_diagnosis)

# if st.button('Heart Test Result'):
#     make_prediction()
    