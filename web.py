import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction Of Disease Outbreaks',
                    layout='wide',
                    page_icon='👩🏻‍⚕️')
diabetes_model=pickle.load(open(r"C:\Users\shris\OneDrive\Desktop\Prediction\Training_Model\diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open(r"C:\Users\shris\OneDrive\Desktop\Prediction\Training_Model\heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"C:\Users\shris\OneDrive\Desktop\Prediction\Training_Model\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected=option_menu('Prediction Of Disease Outbreak System',['Diabetes Prediction','Heart Disease Prediction','Parkinson\'s Prediction'],
                         menu_icon='hospital-fill', icons=['activity','heart','person'], default_index=0)
if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:
        BloodPressure=st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')  
    with col2:
        Age=st.text_input('Age of the Person')  
if selected=='Diabetes Prediction':
    diab_diagnosis=''
    if st.button('Diabetes Test Result'):
            user_input=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, 
                        BMI, DiabetesPedigreeFunction, Age]
            user_input=[float(x) for x in user_input]
            diab_prediction=diabetes_model.predict([user_input])
            if diab_prediction[0]==1:
                diab_diagnosis='The Person Is Diabetic'
            else:
                diab_diagnosis='The Person Is Not Diabetic'
            st.success(diab_diagnosis)

if selected=='Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.text_input('Age')
    with col2:
        Sex=st.text_input('Sex')
    with col3:
        ChestPainTypes=st.text_input('Chest Pain Type')
    with col1:
        RestingBloodPressure=st.text_input('Resting Blood Pressure')
    with col2:
        SerumCholestoral=st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        FastingBloodSugar=st.text_input('Fasting Blood Sugar > 120mg/dl')
    with col1:
        RestingElectrocardiographic=st.text_input('Resting Electrocardiographic Result')
    with col2:
        MaximumHeartRate=st.text_input('Maximum Heart Rate Achieved')
    with col3:
        ExerciseInducedAngina=st.text_input('Exercise Induced Angina')
    with col1:
        STDepressionInduced=st.text_input('ST Depression Induced By Exercise')
    with col2:
        SlopeOfThePeakExercise=st.text_input('Slope Of The Exercise ST Segment')
    with col3:
        MajorVessels=st.text_input('Major Vessels Coloured By Flourosopy')
    with col1:
        Thal=st.text_input('Thal:0=Normal; 1=Fixed Defect; 2=Reversable Defect')

if selected=='Heart Disease Prediction':
    heart_diagnosis=''
    if st.button('Heart Disease Result'):
        user_input=[Age, Sex, ChestPainTypes, RestingBloodPressure, SerumCholestoral,
                    FastingBloodSugar, RestingElectrocardiographic, MaximumHeartRate,
                    ExerciseInducedAngina, STDepressionInduced, SlopeOfThePeakExercise,
                    MajorVessels, Thal]
        user_input=[float(x) for x in user_input]
        heart_disease_prediction=heart_disease_model.predict([user_input])
        if heart_disease_prediction[0]==1:
            heart_diagnosis='The Person Has Heart Disease'
        else:
            heart_diagnosis='The Person Does Not Have Heart Disease'
            st.success(heart_diagnosis)

if selected=='Parkinson\'s Prediction':
    st.title('Parkinson\'s Disease Prediction Using ML')
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        MDVP1=st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP2=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP3=st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVP4=st.text_input('MDVP:Jitter(%)')
    with col5:
        MDVP5=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        MDVP6=st.text_input('MDVP:RAP')
    with col2:
        MDVP7=st.text_input('MDVP:PPQ')
    with col3:
        Jitter=st.text_input('Jitter:DDP')
    with col4:
        MDVP8=st.text_input('MDVP:Shimmer')
    with col5:
        MDVP9=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        Shimmer=st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer2=st.text_input('Shimmer:APQ5')
    with col3:
        MDVP10=st.text_input('MDVP:APQ')
    with col4:
        Shimmer3=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('Spread1')
    with col5:
        spread2=st.text_input('Spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')

if selected=='Parkinson\'s Prediction':
    parkinsons_diagnosis=''
    if st.button('Parkinsons\'s Test Result'):
        user_input=[MDVP1,MDVP2,MDVP3,MDVP4,MDVP5,MDVP6,MDVP7,Jitter,MDVP8,MDVP9,Shimmer,
                    Shimmer2,MDVP10,Shimmer,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        parkinsons_prediction=parkinsons_model.predict([user_input])
        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis='The Person Has Parkinson\'s Disease'
        else:
            parkinsons_diagnosis='The Person Does Not Have Parkinsons\'s Disease'
            st.success(parkinsons_diagnosis)



