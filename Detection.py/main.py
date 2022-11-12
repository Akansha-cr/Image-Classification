from pyrebase import pyrebase
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import io
from PIL import Image
import base64
import pickle

# Configuration Key
firebaseConfig = {
  'apiKey': "AIzaSyD8G9btD0-eGSO876uzaZrFWy74IR7_IoQ",
  'authDomain': "lesion-detection-3d76f.firebaseapp.com",
  'databaseURL': "https://lesion-detection-3d76f-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "lesion-detection-3d76f",
  'storageBucket': "lesion-detection-3d76f.appspot.com",
  'messagingSenderId': "631709653310",
  'appId': "1:631709653310:web:b0f10db7c019f8cf08346f",
  'measurementId': "G-11M83L7HKG"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Welcome")

# Authentication
choice = st.sidebar.selectbox('Signup/login', ['Sign up','Login'])


# App 
title_temp ="""
	<div style="background-color:#4C00A0;padding:9px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">Lesion Detection</h1>
	</div>
	"""
st.markdown(title_temp, unsafe_allow_html= True)
col1,col2= st.columns(2)
with col1:
	st.write(f'<h1 style="color:purple;font-size:35px;">{"Lesion Detection"}</h1>', unsafe_allow_html=True)
	st.markdown(f'<h1 style="color:white;font-size:20px;">{"This website is Dedicated to Detect different types of skin cancer. Please signup or Simply head over to the Analysis and Prediction page to upload an Image and proceed further."}</h1>', unsafe_allow_html=True)
with col2:
	st.image('asset/Site Stats-amico.png')
	
def load_image(image_file):
	img = Image.open(image_file)
	return img

# Sign up Block
if choice == 'Sign up':
	st.markdown(f'<div style="background-color:#7700CB;padding:10px;border-radius:10px;margin:10px; color:white;text-align:center; font-sixe:25px;">{"Create New Account"}</div>', unsafe_allow_html=True)
	st.markdown(f'<h1 style="color:purple;font-size:22px;">{"Enter Email Address"}</h1>', unsafe_allow_html=True)
	email = st.text_input(" ").strip()
	st.markdown(f'<h1 style="color:purple;font-size:22px;">{"Enter a Password"}</h1>', unsafe_allow_html=True)
	password = st.text_input("pass").strip()
	st.markdown(f'<h1 style="color:purple;font-size:22px;">{"Enter a Username"}</h1>', unsafe_allow_html=True)
	handle = st.text_input("username").strip()
	submit = st.button('Create my account')
	if submit:
		user = auth.create_user_with_email_and_password(email, password)
		st.success('Your account is created suceesfully!')
		st.balloons()
		st.title('Welcome' + handle)
		st.info('Login via login drop down selection')
		st.container()
		with st.container():
			st.image('asset/Analytics-amico.png')

		
# Login Block
elif choice == 'Login':
	st.markdown(f'<h1 style="color:white;font-size:28px;">{"Login"}</h1>', unsafe_allow_html=True)
	st.markdown(f'<h1 style="color:white;font-size:18px;">{"Enter Email Address"}</h1>', unsafe_allow_html=True)
	email = st.text_input(" ").strip()
	st.markdown(f'<h1 style="color:white;font-size:18px;">{"Enter your Password"}</h1>', unsafe_allow_html=True)
	password = st.text_input("pass").strip()
	login = st.button('Login')
	if login:
		user = auth.sign_in_with_email_and_password(email,password)
		st.write(f'<h1 style="color:purple;font-size:30px;">{"Please head over to Analysis and Prediction page for Prediction."}</h1>',  unsafe_allow_html=True)
		st.write(f'<h1 style="color:white;font-size:15px;">{"This block is not functional yet, please try again later..."}</h1>',  unsafe_allow_html=True)
		
	
#background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('asset/—Pngtree—abstract background gaming futuristic banner_1235846.jpg')

st.markdown(f'<a href="https://storyset.com/business">Business illustrations by Storyset</a>', unsafe_allow_html=True)


