import streamlit as st
import streamlit.components.v1 as components    
import News_Twitter,Only_News
import Get_data
import models
from PIL import Image
import json
from bs4 import BeautifulSoup

# template = open('home.html')
# soup = BeautifulSoup(template.read(), "html.parser")

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
    st.sidebar.markdown('<img style = "box-shadow: 6px 6px 29px -4px rgba(0, 0, 0, 0.75);" width=290px src="http://drive.google.com/uc?export=view&id=1guCiLr77Ih852eDF__X4kvlHcPo-D94F"/>',unsafe_allow_html=True)
    st.sidebar.markdown('<hr></hr>',unsafe_allow_html=True)
    st.write("Welcome:",username)
    # image = Image.open('logo.png')
    # st.sidebar.image(image,width=200)
    genre = st.sidebar.radio(
     "Options: ",
     ('Home','📰 News','ᓬ News+Social Media','🗺 Explore Models'))    

    country_list = ['India ', 'Russia', ]
    st.sidebar.markdown('<p><b><i><h2>Filters for News</p>',unsafe_allow_html=True)
    all_data = Get_data.column_specific_data('news_Country')
    topic = Get_data.column_specific_data('news_topic') 
    
    topic_selections = st.sidebar.multiselect(
    "Select a Topic", topic,['Business'])

    st.sidebar.markdown("""
        <img src="https://img.icons8.com/clouds/40/000000/small-business.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/globe--v2.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/track-and-field.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/literature.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/robot.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/united-arab-emirates.png"/>
        """
        ,unsafe_allow_html=True)


    country_selections = st.sidebar.multiselect(
    "Select a Country", all_data,['Australia'])

    st.sidebar.markdown("""
        <img src="https://img.icons8.com/clouds/40/000000/india.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/russian-federation.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/china.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/usa.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/germany.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/stethoscope.png"/>
        """
        ,unsafe_allow_html=True)
    
    st.sidebar.markdown("<a href = 'https://docs.google.com/forms/d/e/1FAIpQLSfbS30zIv13_Yo7CnAh0EeP0mued87_qJuwW9mtp9Eugc26fw/viewform?fbzx=-4627928992702263573'>Subscribe to Newsletter</a>",unsafe_allow_html=True)

    st.sidebar.write("All rights reserved BeeNews@2022")

    if genre == 'Home':
        st.write('Home')
        st.title('Overview of our Big Data')
        st.markdown('<iframe  width="1400" height="900" style="background: #F1F5F4;border: none;border-radius: 2px;box-shadow: 0 2px 10px 0 rgba(70, 76, 79, .2);"  src="https://charts.mongodb.com/charts-project-0-hcexa/embed/dashboards?id=6272c95f-8933-41d0-8b88-c7a9b5f3b967&theme=light&autoRefresh=true&maxDataAge=3600&showTitleAndDesc=false&scalingWidth=fixed&scalingHeight=fixed"></iframe>',unsafe_allow_html=True)
        # st.markdown(soup,unsafe_allow_html=True)
    if genre == 'ᓬ News+Social Media':
        News_Twitter.news_main_twitter(country_selections,topic_selections)
    if genre == '📰 News':
        Only_News.news_main(country_selections,topic_selections,username)
    if genre == '🗺 Explore Models':
        models.explore_models()
        st.write("Explore our Models")


        

if __name__ == '__main__':
    main_page()
