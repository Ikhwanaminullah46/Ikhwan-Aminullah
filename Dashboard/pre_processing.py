# File: pre-processing.py


import joblib
import numpy as np
import pandas as pd


pca_1 = joblib.load('model/pca_1.joblib')
pca_2 = joblib.load('model/pca_2.joblib')

encoder_Tuition_fees_up_to_date = joblib.load('model/encoder_Tuition_fees_up_to_date.joblib')
encoder_Course = joblib.load('model/encoder_Course.joblib')
encoder_Scholarship_holder = joblib.load('model/encoder_Scholarship_holder.joblib')
encoder_Gender = joblib.load('model/encoder_Gender.joblib')
encoder_Displaced = joblib.load('model/encoder_Displaced.joblib')
encoder_Application_mode = joblib.load('model/encoder_Application_mode.joblib')
encoder_Previous_qualification = joblib.load('model/encoder_Previous_qualification.joblib')
encoder_Debtor = joblib.load('model/encoder_Debtor.joblib')
encoder_Marital_status = joblib.load('model/encoder_Marital_status.joblib')
encoder_Daytime_evening_attendance = joblib.load('model/encoder_Daytime_evening_attendance.joblib')

scaler_Admission_grade = joblib.load('model/scaler_Admission_grade.joblib')
scaler_Age_at_enrollment = joblib.load('model/scaler_Age_at_enrollment.joblib')
scaler_Curricular_units_1st_sem_approved = joblib.load('model/scaler_Curricular_units_1st_sem_approved.joblib')
scaler_Curricular_units_1st_sem_enrolled = joblib.load('model/scaler_Curricular_units_1st_sem_enrolled.joblib') 
scaler_Curricular_units_1st_sem_evaluations = joblib.load('model/scaler_Curricular_units_1st_sem_evaluations.joblib')
scaler_Curricular_units_1st_sem_grade = joblib.load('model/scaler_Curricular_units_1st_sem_grade.joblib')
scaler_Curricular_units_2nd_sem_approved = joblib.load('model/scaler_Curricular_units_2nd_sem_approved.joblib')
scaler_Curricular_units_2nd_sem_enrolled = joblib.load('model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
scaler_Curricular_units_2nd_sem_evaluations = joblib.load('model/scaler_Curricular_units_2nd_sem_evaluations.joblib')
scaler_Curricular_units_2nd_sem_grade = joblib.load('model/scaler_Curricular_units_2nd_sem_grade.joblib')
scaler_Previous_qualification_grade = joblib.load('model/scaler_Previous_qualification_grade.joblib')

pca_numerical_columns_1 = [
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
]

pca_numerical_columns_2 = [
    'Previous_qualification_grade',
    'Admission_grade',
]

def data_preprocessing(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    df['Marital_status'] = encoder_Marital_status.transform(data['Marital_status'])
    df['Application_mode'] = encoder_Application_mode.transform(data['Application_mode'])
    df['Course'] = encoder_Course.transform(data['Course'])
    df['Previous_qualification'] = encoder_Previous_qualification.transform(data['Previous_qualification'])
    df['Tuition_fees_up_to_date'] = encoder_Tuition_fees_up_to_date.transform(data['Tuition_fees_up_to_date'])
    df['Scholarship_holder'] = encoder_Scholarship_holder.transform(data['Scholarship_holder'])



    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    
    # PCA 1
    data["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    
    df[["pc1_1", "pc1_2", "pc1_3"]] = pca_1.transform(data[pca_numerical_columns_1])
    
    # PCA 2
    data["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]
    data["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))[0]
    
    df[["pc2_1"]] = pca_2.transform(data[pca_numerical_columns_2])
    
    return df