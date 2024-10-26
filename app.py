import streamlit as st
import joblib
import numpy as np

model = joblib.load("mobile.pkl")

st.title = ("App of Prediction")

User_ID  = st.number_input("Please enter your ID:")
Device_Model = st.selectbox("Device Model(0:Xiaomi Mi 11, 1:iPhone 12, 2:Google Pixel 5, 3:OnePlus 9, 4:Samsung Galaxy S21)", [0,1,2,3,4])
App_Usage_Time = st.number_input("Please enter your App Usage Time:")
Screen_On_Time = st.number_input("Please enter your screen on time:")
Battery_Drain = st.number_input("Please enter your Battery Drain")
Number_of_Apps_Installed = st.number_input("Please enter your no of apps installed:")
Data_Usage = st.number_input("Please enter your data usage:")
Age = st.number_input("Please enter your age:")
User_Behavior_Class = ("Please enter your behavior class")
Operating_System = ("Operating System(0:Android, 1:iOS)", [0,1])