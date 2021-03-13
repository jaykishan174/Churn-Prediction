# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:33:28 2021

@author: j.wadhwani
"""

import pickle
from catboost import CatBoostRegressor, Pool

from fuction import *
from sklearn.utils import shuffle
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import cross_val_score, GridSearchCV
import pandas as pd
import streamlit as st

st.title("Employee Churn Prediction")

row_1_2, row_1_3 = st.beta_columns(2)


input_1=row_1_2.number_input("City Development Index",min_value=0.0, step=0.05, max_value=1.0)

input_2=row_1_3.selectbox("Gender", ['Female', 'Male', 'Other'], index=0)

row_2_1, row_2_2, row_2_3 = st.beta_columns(3)

input_3=row_2_1.selectbox("Relevant Experience", ['Has relevent experience','No relevent experience'], index=0)

input_4=row_2_2.selectbox("Enrollment", ['no_enrollment', 'Full time course', 'Part time course'], index=0)

input_11=row_2_3.number_input("Training Hours",min_value=0,step=1)

row_3_1, row_3_2, row_3_3, row_3_4 = st.beta_columns(4)


input_5=row_3_1.selectbox("Education Level", ['Graduate', 'Masters', 'High School', 'Phd', 'Primary School'], index=0)

input_6 =row_3_2.selectbox("Major Discipline", ['STEM', 'Business Degree','Arts', 'Humanities', 'No Major','Other'], index=0)

input_7=row_3_3.number_input("Experience (Years)",min_value=0,step=1)

input_10=row_3_4.number_input("No. of Previous Companies",min_value=0,step=1)

row_4_1, row_4_2 = st.beta_columns(2)

input_9=row_4_1.selectbox("Company Type",['Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other','Public Sector', 'NGO'])

input_8=row_4_2.number_input("Employee Count", min_value=0,step=100)



input_array= [[input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_9, input_10, input_11]]

test=pd.DataFrame(input_array, columns =['city_development_index', 'gender', 'relevent_experience',
       'enrolled_university', 'education_level', 'major_discipline',
       'experience', 'company_size', 'company_type', 'last_new_job',
       'training_hours'])

test['gender'] = test['gender'].apply(gender_to_numeric)
test['relevent_experience'] = test['relevent_experience'].apply(rel_experience)
test['enrolled_university'] = test['enrolled_university'].apply(enrollment)
test['education_level'] = test['education_level'].apply(edu_level)
test['major_discipline'] = test['major_discipline'].apply(major)
test['experience'] = test['experience'].apply(experience)
test['company_type'] = test['company_type'].apply(company_t)
test['company_size'] = test['company_size'].apply(company_s)
test['last_new_job'] = test['last_new_job'].apply(last_job)

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

if st.button("Predict"):
    result = loaded_model.predict(test)
    result_per= round(result[0]*100,2).astype('str')
    result_stm= "The chances of Employee Leaving organisation is: " + result_per + '%'
    st.write(result_stm)
    

