import streamlit as st
import numpy as np
import pandas as pd 
import pickle 
from streamlit_option_menu import option_menu 
import os 

# Set page configuration
st.set_page_config(page_title="Health Gaurd", layout = "wide") 


# Setting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))                                          

parkison_model = pickle.load(open(f'{working_dir}/parkison_model.pkl','rb'))

with st.sidebar:
          selected = option_menu('Disease Detection',['Parkison Detection'])



if selected == 'Parkison Detection':
    st.title("Parkison Disease Detection")

    col1, col2, col3 = st.columns(3)

    with col1:
        Fo_Hz = st.text_input("Enter MDVP:Fo(Hz)")
    with col2:
        Fhi_Hz = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        Flo_Hz = st.text_input("Enter MDVP:Flo(Hz)")
    with col1:
        Jitter_per = st.text_input("Enter Jitter(%)")
    with col2:
        Jitter_Abs = st.text_input("Enter Jitter_Abs")
    with col3:
        rap = st.text_input("Enter RAP")
    with col1:
        ppq = st.text_input("Enter PPQ")
    with col2:
        ddp = st.text_input("Enter DDP")
    with col3:
        shimmer = st.text_input("Enter shimmer ")
    with col1:
        shimmer_db = st.text_input("Enter Shimmer (Db)")
    with col2:
        apq3 = st.text_input("Enter Shimmer (APQ3)")
    with col3:
        apq5 = st.text_input("Enter Shimmer (APQ5)")
    with col1:
        apq = st.text_input("Enter APQ")
    with col2:
        dda = st.text_input("Enter Shimmer: DDA")
    with col3:
        nhr = st.text_input("Enter NHR")
    with col1:
        hnr  = st.text_input("Enter HNR")
    with col2:
        rpde = st.text_input("Enter RPDE")
    with col3:
        dfa = st.text_input("Enter DFA")
    with col1:
        spread1 = st.text_input("Enter Spread1")
    with col2:
        spread2 = st.text_input("Enter Spread 2")
    with col3:
        d2 = st.text_input("Enter D2")
    with col1: 
        ppe = st.text_input("Enter PPE")   
    
    park_diagnosis = ''
               
    # creation of button 
    if st.button('Diabetes Test Result'):
            user_input =[Fo_Hz,Fhi_Hz,Flo_Hz,Jitter_per,Jitter_Abs,
                         rap,ppq, ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]
            
            user_input = [float(x) for x in user_input]

            park_prediction = parkison_model.predict([user_input])

            if park_prediction[0] == 1:
                    park_diagnosis = "The Person is Parkison Positive"
            else:
                park_diagnosis = "The Person is not Parkison Positive" 
    st.success(park_diagnosis)
