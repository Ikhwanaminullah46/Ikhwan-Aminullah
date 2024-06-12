import streamlit as st
import pandas as pd
import joblib

from pre_processing import *
from prediction import prediction

st.title("Student Status Prediction")
st.write("Predicts student enrollment status (Dropout, Enrolled, Graduate).")

st.markdown('## **Inputs**')

col1, col2 = st.columns(2)

with col1:
    Tuition_fees_up_to_date = st.selectbox(label ='Tuition fees up to date',
                                           options = encoder_Tuition_fees_up_to_date.classes_ ,
                                           index = 1
                                           )

    Course = st.selectbox(label = 'Course',
                          options = encoder_Course.classes_,
                          index = 1
    )

    Scholarship_holder = st.selectbox(
        label = 'Scholarship holder',
        options = encoder_Scholarship_holder.classes_,
        index = 1
    )

    Application_mode = st.selectbox(
        label = 'Application Mode',
        options = encoder_Application_mode.classes_,
        index = 1
    )

    Marital_status = st.selectbox(
        label = 'Marital Status',
        options = encoder_Marital_status.classes_,
        index = 1
    )
    Previous_qualification = st.selectbox(
        label = 'Previous Qualification',
        options = encoder_Previous_qualification.classes_,
        index = 1
    )

    Previous_qualification_grade = int(
        st.number_input(
            label = 'Previous Qualification Grade',
            value = 0
        )
    )
    
    Admission_grade = int(
        st.number_input(
            label = 'Admission Grade',
            value = 0
        )
    )



with col2:
    Age_at_enrollment = int(st.number_input(label = 'Age at enrollment',
                                            value = 23
                                            )
                            
                            )
    

    Curricular_units_1st_sem_approved = int(
        st.number_input(
            label = 'Curricular units 1st sem approved',
            value = 0
        )
    )

    Curricular_units_1st_sem_enrolled = int(
        st.number_input(
            label = 'Curricular units 1st sem enrolled',
            value = 0
        )
    )

    Curricular_units_1st_sem_evaluations = int(
        st.number_input(
            label = 'Curricular units 1st sem evaluations',
            value = 0
        )
    )

    Curricular_units_1st_sem_grade = int(
        st.number_input(
            label = 'Curricular units 1st sem grade',
            value = 0
        )
    )

    Curricular_units_2nd_sem_approved = int(
        st.number_input(
            label = 'Curricular units 2nd sem approved',
            value = 0
        )
    )

    Curricular_units_2nd_sem_enrolled = int(
        st.number_input(
            label = 'Curricular units 2nd sem enrolled',
            value = 0
        )
    )

    Curricular_units_2nd_sem_evaluations = int(
        st.number_input(
            label = 'Curricular units 2nd sem evaluations',
            value = 0
        )
    )

    Curricular_units_2nd_sem_grade = int(
        st.number_input(
            label = 'Curricular units 2nd sem grade',
            value = 0
        )
    )

data = pd.DataFrame()

data['Marital_status'] = [Marital_status]
data['Application_mode']  = Application_mode
data['Course']  = Course
data['Previous_qualification']  = Previous_qualification
data['Previous_qualification_grade']  = Previous_qualification_grade
data['Admission_grade']  = Curricular_units_1st_sem_approved
data['Tuition_fees_up_to_date']  = [Tuition_fees_up_to_date]
data['Scholarship_holder']  = Scholarship_holder
data['Age_at_enrollment']  = Age_at_enrollment
data['Curricular_units_1st_sem_approved']  = Curricular_units_1st_sem_approved
data['Curricular_units_1st_sem_enrolled']  = Curricular_units_1st_sem_enrolled
data['Curricular_units_1st_sem_evaluations']  = Curricular_units_1st_sem_evaluations
data['Curricular_units_1st_sem_grade']  = Curricular_units_1st_sem_grade
data['Curricular_units_2nd_sem_approved']  = Curricular_units_2nd_sem_approved
data['Curricular_units_2nd_sem_enrolled']  = Curricular_units_2nd_sem_enrolled
data['Curricular_units_2nd_sem_evaluations']  = Curricular_units_2nd_sem_evaluations
data['Curricular_units_2nd_sem_grade']  = Curricular_units_2nd_sem_grade

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)


if st.button('Predict'):
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Student Status: {}".format(prediction(new_data)))

st.write('Class explanation:')
st.write('1. Dropout = Student failed to complete their study')
st.write('2. Enrolled = Student is still studying and have not graduated yet')
st.write('3. Graduate = Student has successfully finished their study')
