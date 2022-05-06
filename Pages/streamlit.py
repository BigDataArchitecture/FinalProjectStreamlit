import streamlit as st
from matplotlib import pyplot as plt 
from PIL import Image
import streamlit_authenticator as stauth
import main

from datetime import datetime
now = datetime.now()

st.set_page_config(
    page_title="BeeNews",
    page_icon="🎈",
    layout="wide"
)


names = ['John Smith','Rebecca Briggs','parth shah','Admin']
usernames = ['Sreepad','Ankana','Parth','Admin']
passwords = ['Sreepad','Ankana','parth','Admin']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
'some_cookie_name','some_signature_key',cookie_expiry_days=0.01)
name, authentication_status, username = authenticator.login('Login','main')

if authentication_status:
    main.main_page(username)
    st.write("Logged In")
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
