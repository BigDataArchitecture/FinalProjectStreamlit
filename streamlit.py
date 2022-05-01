from tkinter import Button
import streamlit as st
import requests
import json
import numpy as np
from matplotlib import pyplot as plt 
from PIL import Image
import streamlit_authenticator as stauth
from Signup import signup_function
from main import main_page

names = ['John Smith','Rebecca Briggs','parth shah','Admin']
usernames = ['Sreepad','Ankana','Parth','Admin']
passwords = ['Sreepad','Ankana','parth','Admin']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
'some_cookie_name','some_signature_key',cookie_expiry_days=0.01)
name, authentication_status, username = authenticator.login('Login','main')

if authentication_status:
    main_page(authenticator)
    st.write("Logged In")
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
