import streamlit as st
import requests
import json
import numpy as np
from PIL import Image
import streamlit.components.v1 as components    

import pymongo
client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
print(client["UserData"])
db = client["UserData"]
collection = db["Google_News"]
a = collection.find()
count = 1

st.set_page_config(
    page_title="BERT Keyword Extractor",
    page_icon="🎈",
    layout="wide",
)


def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

m1, m2 = st.columns((10,10))
list1 = [m1, m2]
count = 11
news_tit = []
news_summary1 = []
uid = []
links = []
country = []
source = []
for data in a:
    uid.append(data['_id'])
    links.append(data['news_top_image'])
    news_tit.append(data['news_title'])
    news_summary1.append(data['news_summary'])
    country.append(data['news_Country'])
    source.append(data['news_source'])

for i in range(10):
    if count==20:
        break
    else:
        m1,m2,m3 = st.columns((10,10,10))
        list = [m1, m2,m3] 
        for part in list:
            part.write(str(i) + " Aanlysis "+ " Sentiments " + str(i))
            response = requests.get(links[count])
            file = open((str(uid[count])+".png"), "wb")
            file.write(response.content)
            file.close()
            image = Image.open(str(uid[count])+".png")
            part.image(image,width=300)
            part.title(news_tit[count][:70])
            part.write(news_summary1[count])
            part.write(country[count])
            part.write(source[count])
            count = count + 1

        # response = requests.get(data['news_top_image'])
        # file = open(("NewsAggregation/Streamlit/"+str(data['_id'])+".png"), "wb")
        # file.write(response.content)
        # file.close()
        # image = Image.open("NewsAggregation/Streamlit/"+str(data['_id'])+".png")
        # list1[count-1].image(image, caption='Sunrise by the mountains')
        # list1[count-1].write('News Title')
        # list1[count-1].write(data['news_title'])
        # list1[count-1].write('News Summary')
        # list1[count-1].write(data['news_summary'])
        # with list1[count-1].expander("ℹ️ - About this app", expanded=False):
        #     list1[count-1].markdown("")
        # count = 1 + count
        # components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)
