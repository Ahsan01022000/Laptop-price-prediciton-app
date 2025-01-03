import streamlit as st 
import pickle
import pandas as pd
import numpy as np

#importing the model and dataframe
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
 
#Title
st.title("Laptop Price Predicting App")
st.markdown("This App gives you the best prediction for the  laptop prices")

#User Input specifications
st.sidebar.header("Please provide the specifications of the laptop")
Company=st.sidebar.selectbox("Brand",df['Company'].unique())
Type=st.sidebar.selectbox("Type",df['TypeName'].unique())
Ram=st.sidebar.selectbox("Ram(in GB)",df['Ram'].unique())
weight=st.sidebar.number_input("Weight(in Kgs)",min_value=0.0,max_value=5.0,step=0.1)
Touchscreen=st.sidebar.selectbox("Touchscreen",["Yes","No"])
IPS=st.sidebar.selectbox("IPS",["Yes","No"])
Screen_Size=st.sidebar.number_input("Screen Size(in Inches)",min_value=12.0,max_value=17.0,step=0.1)
Resolution=st.sidebar.selectbox("Screen Resolution",["1920x1080","1366x768","1600x900","3840x2160","3200x1800","2880x1800","2560x1600","2560x1440","2304x1440"])
tab1, tab2,tab3,tab4 = st.tabs(["CPU Brand", "GPU Brand","Operating System","Storage"])
with tab1:
    cpu=st.selectbox("CPU Brand",df['Cpu_brand'].unique())
with tab2:
    gpu=st.selectbox("GPU Brand",df['Gpu_Brand'].unique())
with tab3:
   os= st.selectbox("Operating System",df['OS'].unique())
with tab4:
    # Select box for HDD
    hdd= st.selectbox("HDD(in GB)",["0","128","256","512","1024","2048"])
    
    # Select box for SSD
    ssd = st.selectbox("SSD(in GB)",["0","8","128","256","512","1024"])
if st.button("Predict Price"):
    #queru
    if Touchscreen=="Yes":
        Touchscreen=1
    else:
        Touchscreen=0
    if IPS=="Yes":
        IPS=1
    else:
        IPS=0
    X_res=int(Resolution.split("x")[0])
    Y_res=int(Resolution.split("x")[1])
    ppi=((X_res**2)+(Y_res**2))**0.5/Screen_Size
    
    query=np.array([Company,Type,Ram,weight,Touchscreen,IPS,ppi,cpu,hdd,ssd,gpu,os])
    query=query.reshape(1,12)
    st.title("The Predicted Price of the Laptop is Rs." + str(int(np.exp(pipe.predict(query)[0]))))