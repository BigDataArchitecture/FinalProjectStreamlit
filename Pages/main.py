import streamlit as st
import streamlit.components.v1 as components    
import News_Twitter,Only_News
import Get_data
import models
from PIL import Image

st.set_page_config(
    page_title="Twiiter",
    page_icon="🎈",
    layout="wide"
)



def main_page():
    # image = Image.open('logo.png')
    # st.sidebar.image(image,width=200)
    genre = st.sidebar.radio(
     "What do You want to do today?",
     ('📰 News','ᓬ News+Social Media','📊 User Analytics','🗺 Explore Models'))    

    country_list = ['India ', 'Russia', ]
    st.sidebar.markdown('<p style="background-color:powderblue;">Filters for News</p>',unsafe_allow_html=True)
    all_data = Get_data.column_specific_data('news_Country')
    country_selections = st.sidebar.multiselect(
    "Select a Country", all_data,['India '])
    st.sidebar.markdown("""
        <img src="https://img.icons8.com/clouds/40/000000/india.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/russian-federation.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/china.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/usa.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/germany.png"/>
        <img src="https://img.icons8.com/clouds/40/000000/united-arab-emirates.png"/>
        """
        ,unsafe_allow_html=True)
    if genre == 'ᓬ News+Social Media':
        News_Twitter.news_main_twitter(country_selections)
    if genre == '📰 News':
        Only_News.news_main(country_selections)
    if genre == '📊 User Analytics':
        st.write("User Analytics")
        if st.button("Clicl me"):
            st.write("Smart")
    if genre == '🗺 Explore Models':
        models.explore_models()
        st.write("Explore our Models")

        

if __name__ == '__main__':
    main_page()
