import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Doctor Consultation',
                            'Emergency Alert'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            #diab_diagnosis = 'You are diagonsed with diabetes\n \n '
            st.markdown('<p style="color:red; border-radius: 25px">                       <b>&nbsp;&nbsp;&nbsp;&nbsp;You are diagonsed with diabetes<b><br>                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;Preventive measures:  <br>                                                                               --> Healthy Eaten<br>                                                                                                                   --> Regular Physical Activities<br>                                                                                                          --> Avoid Sugary Beverages<br>                                                                                                          --> Regular Health Checkup<br>                                                                                                                             --> Manage Stress</p>', unsafe_allow_html=True)
        else:
            st.success('You are not diagonsed with diabetes')

    #st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            st.markdown('<p style="color:red; border-radius: 25px">                        <b>&nbsp;&nbsp;&nbsp;&nbsp;You are diagnosed with heart disease.<b><br>                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;Preventive measures: <br>                                                                               &nbsp;&nbsp;&nbsp;&nbsp;--> Regular Exercise<br>                                                                                                                      &nbsp;&nbsp;&nbsp;&nbsp;--> Maintain a healthy weight<br>                                                                                                         &nbsp;&nbsp;&nbsp;&nbsp;--> Manage Stress<br>                                                                                                                             &nbsp;&nbsp;&nbsp;&nbsp;--> Get Enough Sleep</p>', unsafe_allow_html=True)
        else:
            st.success('The person does not have any heart disease')

    #st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            #parkinsons_diagnosis = "You are diagonsed with Parkinson's disease. Please take these preventive measures.<br> --> Regular exersice <br> --> Healthy Diet<br> --> Adequate Vitamin-D<br> --> Manage Stress"
            st.markdown('<p style="color:red; border-radius: 25px">                       <b>&nbsp;&nbsp;&nbsp;&nbsp;You are diagonsed with Parkinsons disease.<b><br>                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;Please take these preventive measures:<br>                                                                                                     &nbsp;&nbsp;&nbsp;&nbsp;--> Regular exersice <br>                                                                                                        &nbsp;&nbsp;&nbsp;&nbsp;--> Healthy Diet<br>                                                                                                                       &nbsp;&nbsp;&nbsp;&nbsp;--> Adequate Vitamin-D<br>                                                                                                                   &nbsp;&nbsp;&nbsp;&nbsp;--> Manage Stress     </p>', unsafe_allow_html=True)
        else:
            st.success('You are not diagonsed with Parkinsons disease.')

    #st.success(parkinsons_diagnosis)


# Doctor's Consultation Group
if selected == 'Doctor Consultation':
    st.title('Doctor Consultation ')
    col1, col2, col3, col4, col5 = st.columns(5)
    #row1, row2, row3 = st.rows(3)
    
    with col1:
        st.write('Name: Dr Gautam Naik' )
        st.write('Type: Cardiologist')
        st.write('Doctor Phone no:+91 8069305511')
        st.write('Doctor Experience: 12 Year')
        st.write('Doctor Hospital: NH-19, South East Delhi, New Delhi, 110076')

    with col2:
        st.write('Name: Dr Amit Mittal' )
        st.write('Type: Cardiologist')
        st.write('Doctor Phone no:+91 8062207719')
        st.write('Doctor Experience: 11 Year')
        st.write('Doctor Hospital: Apollo Hospitals Indraprastha, New Delhi')

    with col3:
        st.write('Name: Dr Gaurav Gupta' )
        st.write('Type: Diabetologist')
        st.write('Doctor Phone no:+91 08800737264')
        st.write('Doctor Experience: 8 Year')
        st.write('Doctor Hospital: Galaxy Royal Shoppe Gaur City 2, Greater Noida UP, 201009')
    
    with col4:
        st.write('Name: Dr Harsh Bardhan ')
        st.write('Type: Diabetologist')
        st.write('Doctor Phone no:+91 9917XXXXXX')
        st.write('Doctor Experience: 10 Year')
        st.write('Doctor Hospital: 112 City Plaza, Gaur City-1, Sector 4, Noida, UP, 201009')

    with col5:
        st.write('Name: Dr Mohit Bhatt' )
        st.write('Type: Neurology')
        st.write('Doctor Phone no:+91 8010994994')
        st.write('Doctor Experience: 38 Year')
        st.write('Doctor Hospital: Kokilaben Dhirubani Hospital, Andheri, Mumbai')
    
    with col1:
        st.write('Name: Dr Debashis Bhattacharyya' )
        st.write('Type: Neurology')
        st.write('Doctor Phone no:+91 8010994994')
        st.write('Doctor Experience: 22 Year')
        st.write('Doctor Hospital: Narayana Multispeciality Hospital, Howrah, Kolkata')

    with col2:
        st.write('Name: Dr Ajay Nihalani' )
        st.write('Type: Psychiatrist')
        st.write('Doctor Phone no:+91 08130491951')
        st.write('Doctor Experience: 12 Year')
        st.write('Doctor Hospital: Rajhans Plaza, Ahinsa Khand-i, Indrapuram, Ghaziabad, UP')

    with col3:
        st.write('Name: Dr Kapil K Singhal' )
        st.write('Type: Neurologist')
        st.write('Doctor Phone no:+91 9087898765')
        st.write('Doctor Experience: 22 Year')
        st.write('Doctor Hospital: 135, Opposite Avantika Hospital, Niti Khand 2, Ghaziabad, UP')
    
    with col4:
        st.write('Name: Dr. (Lt Den) CS Narayanan' )
        st.write('Type: Neurologist')
        st.write('Doctor Phone no:+91 8372553627')
        st.write('Doctor Experience: 12 Year')
        st.write('Doctor Hospital: Manipal Hospital, Ghaziabad')


# Emergency Alert
if selected == 'Emergency Alert':
    st.title('Emergency Alert')
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # HTML with inline CSS
    with col1:
        st.markdown('<p style="color:red; font-size: 28px;"><b>Working on...</b></p>', unsafe_allow_html=True)
    
    
    
    
    
    
    
    
