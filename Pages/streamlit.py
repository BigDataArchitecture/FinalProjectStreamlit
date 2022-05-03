from tkinter import Button
import streamlit as st
import requests
import json
import numpy as np
from matplotlib import pyplot as plt 
from PIL import Image
import streamlit_authenticator as stauth
import main
from google.cloud import bigquery
from google.oauth2 import service_account

with open('bigdata-assignment-340502-766cad4a3cbf.json') as source:
    info = json.load(source)

credentials = service_account.Credentials.from_service_account_info(info)
projectid = "bigdata-assignment-340502"
client = bigquery.Client(credentials= credentials,project=projectid)

from datetime import datetime
now = datetime.now()

st.set_page_config(
    page_title="BERT Keyword Extractor",
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
    query = """INSERT INTO `bigdata-assignment-340502.news_user_details.user_logins` VALUES ({},'{}','{}','{}','{}','{}') """.format(1,'parth','Shah',username,'parth981gmail.com',now)
    query_job = client.query(query)
    st.write("Logged In")
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
