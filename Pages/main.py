import streamlit as st
import streamlit.components.v1 as components    
import News_Twitter,Only_News
import Get_data
import models
from PIL import Image
from google.cloud import bigquery
from google.oauth2 import service_account
import json

# from datetime import datetime
# now = datetime.now()

# with open('bigdata-assignment-340502-766cad4a3cbf.json') as source:
#     info = json.load(source)

# credentials = service_account.Credentials.from_service_account_info(info)
# projectid = "bigdata-assignment-340502"
# client = bigquery.Client(credentials= credentials,project=projectid)

# st.set_page_config(
#     page_title="Twiiter",
#     page_icon="🎈",
#     layout="wide"
# )



def main_page(username):
    st.write("Welcome:",username)
    # image = Image.open('logo.png')
    # st.sidebar.image(image,width=200)
    genre = st.sidebar.radio(
     "What do You want to do today?",
     ('Home','📰 News','ᓬ News+Social Media','📊 User Analytics','🗺 Explore Models'))    

    country_list = ['India ', 'Russia', ]
    st.sidebar.markdown('<p style="background-color:powderblue;">Filters for News</p>',unsafe_allow_html=True)
    all_data = Get_data.column_specific_data('news_Country')
    topic = Get_data.column_specific_data('news_topic') 
    
    topic_selections = st.sidebar.multiselect(
    "Select a Topic", topic,['Business'])

    country_selections = st.sidebar.multiselect(
    "Select a Country", all_data,['Australia'])

    st.sidebar.markdown("""
        <img src="https://img.icons8.com/clouds/40/000000/india.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/russian-federation.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/china.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/usa.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/germany.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/united-arab-emirates.png"/>
        """
        ,unsafe_allow_html=True)
    if genre == 'Home':
        st.write('Home')
    if genre == 'ᓬ News+Social Media':
        News_Twitter.news_main_twitter(country_selections,topic_selections)
    if genre == '📰 News':
        Only_News.news_main(country_selections,topic_selections,username)
    if genre == '📊 User Analytics':
        st.write("User Analytics")
        if st.button("Clicl me"):
            st.write("Smart")
    if genre == '🗺 Explore Models':
        models.explore_models()
        st.write("Explore our Models")

        

if __name__ == '__main__':
    main_page()
