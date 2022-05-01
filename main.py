import streamlit as st
import requests
import json
import numpy as np
from PIL import Image
import streamlit.components.v1 as components    
import pymongo
from full_article import full_article_function


st.set_page_config(
    page_title="BERT Keyword Extractor",
    page_icon="🎈",
    layout="wide",
)

def main_page(authenticator):
    authenticator.logout('Logout', 'main')
    st.sidebar.markdown('<h1 style="text-align:center">News Aggregator</h1>', unsafe_allow_html=True)
    st.sidebar.markdown('<hr style="border-left: 2000px solid green; size: 200px"> </hr>', unsafe_allow_html=True)

    st.sidebar.button("Models")

    client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
    print(client["News"])
    db = client["News"]
    collection = db["GoogleAPI"]
    a = collection.find()
    count = 0


    def change(keyword, color = True):
        if color:
            if keyword == 'NEU':
                return 'Blue'
            if keyword == 'NEG':
                return 'Red'
            if keyword == 'POS':
                return 'Green'
        else:
            if keyword == 'NEU':
                return 'Neutral'
            if keyword == 'NEG':
                return 'Negative'
            if keyword == 'POS':
                return 'Positive'



    def keyword_beautificaiton(list1):
        concat =  ""
        for i in range(4):
            concat = concat + " " + list1[i].upper()
        return concat




    m1, m2 = st.columns((10,10))
    list1 = [m1, m2]
    count = 1
    news_tit = []
    news_summary1 = []
    uid = []
    links = []
    country = []
    source = []
    sentiments = []
    text_sentiments = []
    keywords_list = []
    for data in a:
        try:
            uid.append(data['_id'])
            links.append(data['news_top_image'])
            news_tit.append(data['news_title'])
            news_summary1.append(data['news_summary'])
            country.append(data['news_Country'])
            source.append(data['news_source'])
            keywords_list.append(data['news_keywords'])
            try:
                sentiments.append(data['news_sentiments'][0]['score'])
                text_sentiments.append(data['news_sentiments'][0]['label'])
            except:
                sentiments.append(data['news_sentiments'])
                text_sentiments.append(data['news_sentiments'])

        except:
            continue


    for i in range(4):
        if count==12:
            break
        else:
            m1,m2,m3 = st.columns((10,10,10))
            list = [m1, m2,m3] 
            for part in list:
                part.markdown('<p style="font-family:Times New Roman; color: '+change(text_sentiments[count], color = True)+'; font-size: 20px;">' + change(text_sentiments[count], color = False) + " "+ str(round(sentiments[count]*100,2)) + "%"  + '</p>', unsafe_allow_html=True)
                # part.markdown('<p style="font-family:Times New Roman; color:Red; font-size: 20px;">' + str(text_sentiments[count]) + str(sentiments[count]) + '</p>', unsafe_allow_html=True) 
                with part.expander("ℹ️ - About this app", expanded=False):
                    part.write(keyword_beautificaiton(keywords_list[count]))
                response = requests.get(links[count])
                file = open("images/" + (str(uid[count])+".png"), "wb")
                file.write(response.content)
                file.close()
                image = Image.open("images/" + str(uid[count])+".png")
                part.image(image,width=300)
                part.subheader(news_tit[count][:70])
                part.write(news_summary1[count])
                part.write(country[count])
                part.write(source[count])
                if part.button('Read Full Article',key = count):
                    part.write("Cool")
                    full_article_function()

                count = count + 1
            st.markdown('<hr style="border-left: 6px solid green;">  </hr>', unsafe_allow_html=True)

if __name__ == '__main__':
    main_page()
