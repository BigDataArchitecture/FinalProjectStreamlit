import streamlit as st
import streamlit.components.v1 as components    
import News_Twitter,Only_News
import Get_data

st.set_page_config(
    page_title="Twiiter",
    page_icon="🎈",
    layout="wide"
)

def main_page():
    country_list = ['India ', 'Russia']
    # all_data = Get_data.column_specific_data('news_Country')
    country_selections = st.sidebar.multiselect(
    "Select Accounts to View", country_list,['India '])
    st.sidebar.markdown('<img src="https://img.icons8.com/external-sbts2018-flat-sbts2018/30/000000/external-india-gate-monuments-sbts2018-flat-sbts2018.png"/><img src="https://img.icons8.com/clouds/30/000000/russian-federation.png"/>',unsafe_allow_html=True)
    genre = st.sidebar.radio(
     "Select a Viewing Mode",
     ('Original','Social Media'))    
    if genre == 'Social Media':
        News_Twitter.news_main_twitter(country_selections)
    else:
        Only_News.news_main(country_selections)

if __name__ == '__main__':
    main_page()
