import streamlit as st
import joblib
import numpy as np

model = joblib.load("mobile.pkl")

st.title("App of Prediction")

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



#            User_ID = st.text_input("User ID")
 #           Device_Model = st.text_input("Device Model")
  #          App_Usage_Time = st.number_input("App Usage Time", min_value=0.0)
   #         Screen_On_Time = st.number_input("Screen On Time", min_value=0.0)
    #        Battery_Drain = st.number_input("Battery Drain", min_value=0.0)
     #       Number_of_Apps_Installed = st.number_input("Number of Apps Installed", min_value=0)
      #      Data_Usage = st.number_input("Data Usage", min_value=0.0)
       #     Age = st.number_input("Age", min_value=0)
       #     User_Behavior_Class = st.text_input("User Behavior Class")
        #    Operating_System = st.text_input("Operating System")


if st.button("predict"):
    # Create an array of features for prediction
    features = np.array([[User_ID, Device_Model, App_Usage_Time, 
                          Screen_On_Time, Battery_Drain, 
                          Number_of_Apps_Installed, Data_Usage, 
                          Age, User_Behavior_Class, 
                          Operating_System]])
    
    try:
        result = model.predict(features)
        st.write("Prediction:", result)
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")