from prometheus_client import Summary
import streamlit as st
import Get_data
from helper import change,keyword_beautificaiton,get_image,clear_summary
from PIL import Image
import json
import email_html
from bokeh.models.widgets import Div
from datetime import datetime
now = datetime.now()
 



def news_main(country_selections,topic_selections,username):
    all_data = Get_data.filter_data(country_selections,topic_selections)
    def news_beautification(column,news_title,news_sentiment_score,news_sentiment_text,keywords,save_path,summary,country,source):
        image = Image.open(save_path)
        column.image(image,width=360)
        column.markdown('<style> .intro{ width: 360px;border: 3px solid #1DA1F2; padding: 10px;}</style><div class="intro"><p style="font-family:Times New Roman; color: '
        + change(news_sentiment_text, color = True)+'; font-size: 20px;">' 
        + change(news_sentiment_text, color = False) + " "+ news_sentiment_score + "%"  + '</p>'+ keywords + '<h4>'
        + news_title + '</h4><p style = "text-align: justify;text-justify: inter-word;">'+summary+
        '<p>' + '📍' + '<i><u>' + country + '</i></u>'+' ℹ️ ' + source + '</div>'
        ,unsafe_allow_html=True)

    news_links = []
    news_tit = []
    news_summary1 = []
    uid = []
    links = []
    country = []
    source = []
    sentiments = []
    text_sentiments = []
    keywords_list = []
    counter_data = 1
    for data in all_data:
        if counter_data == 17:
            break
        else:
            news_links.append(data['news_link'])
            uid.append(data['_id'])
            links.append(data['news_top_image'])
            news_tit.append(data['news_title'])
            if clear_summary(data['news_summary']):
                news_summary1.append(data['news_summary'])
            else:
                continue
            country.append(data['news_Country'])
            source.append(data['news_source'])
            keywords_list.append(data['news_keywords'])
            try:
                sentiments.append(data['news_sentiments'][0]['score'])
                text_sentiments.append(data['news_sentiments'][0]['label'])
            except:
                sentiments.append(data['news_sentiments'])
                text_sentiments.append(data['news_sentiments'])
            counter_data = counter_data + 1

    print(news_links)
    count = 0
    if len(sentiments) == 0:
        st.write("Sorry No news for this Filter")
    else:

        for data in range(5):
            if count == len(sentiments):
                break
            else:
                try:
                    print("Started",count)
                    m1,m2,m3 = st.columns((10,10,10))
                    list = [m1, m2,m3]
                    for part in list:
                        news_sentiment_score = str(round(sentiments[count]*100,2))
                        news_sentiment_text = text_sentiments[count]
                        save_path = get_image(links[count],uid[count])
                        news_beautification(part,news_tit[count],news_sentiment_score,news_sentiment_text,keyword_beautificaiton(keywords_list[count]),save_path,news_summary1[count],country[count],source[count])
                        if part.button("Read Full Article",key = count): 
                            js = "window.open('" + news_links[count]+"')"  # New tab or window
                            # js = "window.location.href = '"+news_links[count]+"'" # Current tab
                            html = '<img src onerror="{}">'.format(js)
                            print(html)
                            div = Div(text=html)
                            st.bokeh_chart(div)
                            # email_html.email(news_tit[count],news_sentiment_score,change(news_sentiment_text,color= False),keyword_beautificaiton(keywords_list[count]),news_summary1[count],source[count],links[count])
                            # st.markdown(st.markdown('<iframe width="120" src="https://twitter.com/johnebhome/status/1520131611110563840"></iframe>', unsafe_allow_html=True))
                        count = count + 1
                    st.write('----------------------------------------')
                except:
                    continue

    
if __name__ == '__main__':
    news_main()