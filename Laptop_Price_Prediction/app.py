import streamlit as st
import pickle
import numpy as np
pipe = pickle.load(open(r'Laptop_Price_Prediction\pipe.pkl','rb'))
df =pickle.load(open(r'Laptop_Price_Prediction\df.pkl','rb'))

st.title("Laptop Price Predictor")
company = st.selectbox('Brand',df['Company'].unique())       
type_name = st.selectbox('Type',df['TypeName'].unique())              
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])
Weight = st.number_input('Weight of the Laptop(in Kg)')
touchscreen = st.selectbox('TouchScreen',['No','Yes'])
ips = st.selectbox('IPS',['No','Yes'])
screen_size = st.number_input('Screen_Size(in inches)')
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('CPU',df['Processor_type'].unique())                
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD(in GB)',[0,128,256,512,1024])
gpu = st.selectbox('GPU',df['GPU_brand'].unique())              
os = st.selectbox('OS',df['OpSys'].unique())
if st.button('Predict Price'):
    ppi = None
    if touchscreen =='Yes':
       touchscreen = 1
    else:
        touchscreen=0
    if ips =='Yes':
        ips=1
    else: ips=0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    if screen_size > 0:
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
    else:
        st.error("Screen size must be greater than 0.")
        st.stop()

    query = np.array([company,type_name,ram,os,Weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu])

    query = query.reshape(1,12)
    # st.title(np.exp(pipe.predict(query)))
    st.title(f"Predicted Price: ₹ {pipe.predict(query)[0]:,.0f}")