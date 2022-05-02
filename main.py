import streamlit as st
import streamlit.components.v1 as components    
import News_Twitter,Only_News
import Get_data

# st.set_page_config(
#     page_title="Twiiter",
#     page_icon="🎈",
#     layout="wide"
# )

def main_page():
    all_data = Get_data.column_specific_data('news_Country')
    country_selections = st.sidebar.multiselect(
    "Select Accounts to View", all_data,all_data[0])
    genre = st.sidebar.radio(
     "Select a Viewing Mode",
     ('Original','Social Media'))    
    if genre == 'Social Media':
        News_Twitter.news_main_twitter(country_selections)
    else:
        Only_News.news_main(country_selections)

if __name__ == '__main__':
    main_page()
