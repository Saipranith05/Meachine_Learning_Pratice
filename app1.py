import streamlit as st
import joblib
import numpy as np

model = joblib.load("Mobiles.pkl")

st.title("App of Prediction")
st.image("WhatsApp.jpeg")


user_id = st.number_input("Please enter your ID:")
device_model = st.selectbox("Device Model (0:Xiaomi Mi 11, 1:iPhone 12, 2:Google Pixel 5, 3:OnePlus 9, 4:Samsung Galaxy S21)", [0, 1, 2, 3, 4])
app_usage_time = st.number_input("Please enter your App Usage Time:")
screen_on_time = st.number_input("Please enter your Screen On Time:")
battery_drain = st.number_input("Please enter your Battery Drain:")
number_of_apps_installed = st.number_input("Please enter your number of apps installed:")
data_usage = st.number_input("Please enter your Data Usage:")
age = st.number_input("Please enter your Age:")
feature11 = 0
# Use a selectbox for user behavior class input
user_behavior_class = st.number_input("Please enter your behavior class (e.g., 0, 1, 2):", step=1)
operating_system = st.selectbox("Operating System (0:Android, 1:iOS)", [0, 1])

# When the predict button is clicked
if st.button('predict'):
    features = np.array([[user_id, device_model, app_usage_time, screen_on_time, battery_drain, 
                          number_of_apps_installed, data_usage, age, user_behavior_class, operating_system,feature11]])
    
    output = model.predict(features)
    
    # Display the prediction result
    st.write(f" The Predict: {'Male' if output == 1 else 'Female'}")