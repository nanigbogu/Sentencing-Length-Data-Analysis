from pyexpat import model
import streamlit as st
import numpy as np
import pickle
import time
import pandas as pd

st.set_page_config(layout="wide")

st.title("Prison Sentence Length Predictor")
st.header("Specify Characteristics to See Effect\
    on Sentence Length")


col1, col2 = st.columns(2)
st.write('')
st.write('')
col3,col4,col5,col6 = st.columns(4)
st.write('')
st.write('')
col7,col8,col9 = st.columns(3)
st.write('')
st.write('')
col10,col11 = st.columns(2)
st.write('')
st.write('')
col12, col13,col14 = st.columns(3)
st.write('')
st.write('')

with col1:
    year_sent= st.selectbox('Year Sentenced',['2018','2019','2020','2021'])
with col2:
    state= st.selectbox('State',['Alabama','Alaska','Arizona','Arkansas','California',
    'Colorado','Connecticut','Delaware','Florida','Georgia',
    'Hawaii','Idaho','Illinois','Indiana','Iowa',
    'Kansas','Kentucky','Louisiana','Maine','Maryland',
    'Massachusetts','Michigan','Minnesota','Mississippi',
    'Missouri','Montana','Nebraska','Nevada','New Hampshire',
    'New Jersey','New Mexico','New York','North Carolina',
    'North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania',
    'Rhode Island','South Carolina','South Dakota','Tennessee',
    'Texas','Utah','Vermont','Virginia','Washington',
    'West Virginia','Wisconsin','Wyoming'])

with col3:
    age= st.number_input('Age',min_value = 16,max_value=93)
with col4:
    gender = st.selectbox('Gender',['Male','Female'])
with col5:
    race= st.selectbox('Race',['White','African-American','Hispanic','Native American/Alaskan Native',
    'Asian-American or Pacific Islander','Multi-Racial'])
with col6:
    citizen= st.selectbox('U.S. Citizen',['Yes','No'])

with col7:
    dependents= st.selectbox('Dependents',['Yes','No'])
with col8:
    college= st.selectbox('Some College',['Yes','No'])
with col9:
    criminal_history= st.selectbox('Criminal History',['Yes','No'])

with col10:
    disposition= st.selectbox('Trial/Plea',['Guily Plea','No Contest','Jury Trial','Judge Trial',
    'Guilty Plea and Trial'])
with col11:
    presentence= st.selectbox('Pre-Sentence Detention Status',['In Custody','On Bail',
    'Released on Own Recognizance','Other'])

with col12:
    crime_type= st.selectbox('Primary Offense (Offense Carrying Largest Min. Sentence)',['Administration of Justice','Antitrust','Arson',
'Assault','Bribery/Corruption','Burglary/Trespass',
'Child Pornography','Commercialized Vice','Drug Possession',
'Drug Trafficking','Environmental','Extortion/Racketeering',
'Firearms','Food and Drug','Forgery/Counter/Copyright',
'Fraud/Theft/Embezzlement','Immigration','Individual Rights',
'Kidnapping','Manslaughter','Money Launder','Murder',
'National Defense','Obscenity/Other Sex Offenses',
'Prison Offenses','Robbery','Sex Abuse','Stalking/Harassing'
'Tax','Other'])
with col13:
    drug_type= st.selectbox('Drug Type',['None', 'Cocaine','Crack','Heroin','Marijuana',
    'Methamphetamine','Fentanyl','Other'])
with col14:
    weapon= st.selectbox('Use or Possession of Firearm During Crime',['Yes','No'])


user_input = np.array([[year_sent,gender,dependents,college,race,disposition,
    citizen,state,criminal_history,drug_type,age,weapon,presentence,crime_type]])

with open("./data/saved_lasso_sent_model.pkl", "rb") as f:
    lasso_pipe = pickle.load(f)

def sent_predicter(pred_model,user_input):
    
    user_input_code = {}
    
    user_input_code['year_sentenced'] = int(year_sent)

    user_input_code['sentence_type'] = 1 #sentence type set for prison

    user_input_code['imprisoned'] = 1   #imprisoned, yes

    if dependents == 'Yes':
        user_input_code['dependents'] = 1
    else:
        user_input_code['dependents'] = 0

    user_input_code['count_convictons'] = (1) #count convictions being set to 1
    
    if race == 'White':
        user_input_code['race'] = 1
    elif race == 'African-American':
        user_input_code['race'] = 2
    elif race == 'Hispanic':
        user_input_code['race'] = 0
    elif race == 'Native American/Alaskan Native':
        user_input_code['race'] = 3
    elif race == 'Asian-American or Pacific Islander':
        user_input_code['race'] = 4
    elif race == 'Multi-Racial':
        user_input_code['race'] = 7

    if disposition == 'Guily Plea':
        user_input_code['disposition'] = 1
    elif disposition == 'No Contest':
        user_input_code['disposition'] = 2
    elif disposition == 'Jury Trial':
        user_input_code['disposition'] = 3
    elif disposition == 'Judge Trial':
        user_input_code['disposition'] = 4
    elif disposition == 'Guilty Plea and Trial':
        user_input_code['disposition'] = 5

    if citizen == 'Yes':
        user_input_code['citizen'] = 1
    else:
        user_input_code['citizen'] = 0

    user_input_code['state'] = state
    
    if criminal_history == 'Yes':
        user_input_code['criminal_hist'] = 1
    else:
        user_input_code['criminal_hist'] = 0
    
    if drug_type == 'None':
        user_input_code['drug_type'] = 0
    elif drug_type == 'Cocaine':
        user_input_code['drug_type'] = 1
    elif drug_type == 'Crack':
        user_input_code['drug_type'] = 2
    elif drug_type == 'Heroin':
        user_input_code['drug_type'] = 3
    elif drug_type == 'Marijuana':
        user_input_code['drug_type'] = 4
    elif drug_type == 'Methamphetamine':
        user_input_code['drug_type'] = 6
    elif drug_type == 'Fentanyl':
        user_input_code['drug_type'] = 7
    # elif drug_type == 'Other':
    #     user_input_code['drug_type'] = 77

    user_input_code['case_type'] = 1   #case_type is only felony

    user_input_code['age'] = age  #add age to the array
    
    if weapon == 'Yes':
        user_input_code['weapon'] = 1
    else:
        user_input_code['weapon'] = 0

    if presentence == 'In Custody':
        user_input_code['presentence_stat'] = 1
    elif presentence == 'On Bail':
        user_input_code['presentence_stat'] = 2
    elif presentence == 'Released on Own Recognizance':
        user_input_code['presentence_stat'] = 3
    # elif presentence == 'Other':
    #     user_input_code['presentence_stat'] = 4
    
    if gender == 'Male':
        user_input_code['gender'] = 0
    else:
        user_input_code['gender'] = 1
    

    if crime_type == 'Administration of Justice':
        user_input_code['crime_type'] = 1
    elif crime_type == 'Antitrust':
        user_input_code['crime_type'] = 2
    elif crime_type == 'Arson':
        user_input_code['crime_type'] = 3
    elif crime_type == 'Assault':
        user_input_code['crime_type'] = 4
    elif crime_type == 'Bribery/Corruption':
        user_input_code['crime_type'] = 5
    elif crime_type == 'Burglary/Trespass':
        user_input_code['crime_type'] = 6
    elif crime_type == 'Child Pornography':
        user_input_code['crime_type'] = 7
    elif crime_type == 'Commercialized Vice':
        user_input_code['crime_type'] = 8
    elif crime_type == 'Drug Possession':
        user_input_code['crime_type'] = 9
    elif crime_type == 'Drug Trafficking':
        user_input_code['crime_type'] = 10
    elif crime_type == 'Environmental':
        user_input_code['crime_type'] = 11
    elif crime_type == 'Extortion/Racketeering':
        user_input_code['crime_type'] = 12
    elif crime_type == 'Firearms':
        user_input_code['crime_type'] = 13
    elif crime_type == 'Food and Drug':
        user_input_code['crime_type'] = 14
    elif crime_type == 'Forgery/Counter/Copyright':
        user_input_code['crime_type'] = 15
    elif crime_type == 'Fraud/Theft/Embezzlement':
        user_input_code['crime_type'] = 16
    elif crime_type == 'Immigration':
        user_input_code['crime_type'] = 17
    elif crime_type == 'Individual Rights':
        user_input_code['crime_type'] = 18
    elif crime_type == 'Kidnapping':
        user_input_code['crime_type'] = 19
    elif crime_type == 'Manslaughter':
        user_input_code['crime_type'] = 20
    elif crime_type == 'Money Launder':
        user_input_code['crime_type'] = 21
    elif crime_type == 'Murder':
        user_input_code['crime_type'] = 22
    elif crime_type == 'National Defense':
        user_input_code['crime_type'] = 23
    elif crime_type == 'Obscenity/Other Sex Offenses':
        user_input_code['crime_type'] = 24
    elif crime_type == 'Prison Offenses':
        user_input_code['crime_type'] = 25
    elif crime_type == 'Robbery':
        user_input_code['crime_type'] = 26
    elif crime_type == 'Sex Abuse':
        user_input_code['crime_type'] = 27
    elif crime_type == 'Stalking/Harassing':
        user_input_code['crime_type'] = 28
    elif crime_type == 'Tax':
        user_input_code['crime_type'] = 29
    # elif crime_type == 'Other':
    #     user_input_code['crime_type'] = 30

    if college == 'Yes':
        user_input_code['college'] = 1
    else:
        user_input_code['college'] = 0

    model_pred = pred_model.predict(pd.DataFrame(user_input_code,index=[0]))
    if model_pred < 0:
        return 0
    if model_pred > 0:
        return float(np.round((model_pred/12),1))
    # return prediction

with st.spinner("Predicting..."):
    time.sleep(2)
    prediction = sent_predicter(lasso_pipe, user_input)
st.title('The predicted sentence length is '+str(prediction)+' years.')