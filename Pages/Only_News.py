import streamlit as st
import Get_data
from helper import change,keyword_beautificaiton,get_image
from PIL import Image


def news_main():
    all_data = Get_data.access_data()
    # all_data = Get_data.filter_data(country_selections)
    def news_beautification(column,news_title,news_sentiment_score,news_sentiment_text,keywords,save_path,summary,country,source):
        image = Image.open(save_path)
        column.image(image,width=400)
        column.markdown('<style> .intro{ width: 400px;border: 3px solid #1DA1F2; padding: 10px;}</style><div class="intro"><p style="font-family:Times New Roman; color: '
        + change(news_sentiment_text, color = True)+'; font-size: 20px;">' 
        + change(news_sentiment_text, color = False) + " "+ news_sentiment_score + "%"  + '</p>'+ keywords + '<h4>'
        + news_title + '</h4><p style = "text-align: justify;text-justify: inter-word;">'+summary+
        '<p>' + '📍' + '<i><u>' + country + '</i></u>'+' ℹ️ ' + source + '</div>'
        ,unsafe_allow_html=True)

    news_tit = []
    news_summary1 = []
    uid = []
    links = []
    country = []
    source = []
    sentiments = []
    text_sentiments = []
    keywords_list = []
    for data in all_data:
        print(data['news_title'])
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

    count = 1
    for data in range(12):
        if count == 12:
            break
        else:
            try:
                m1,m2,m3 = st.columns((10,10,10))
                list = [m1, m2,m3]
                for part in list:
                    news_sentiment_score = str(round(sentiments[count]*100,2))
                    news_sentiment_text = text_sentiments[count]
                    save_path = get_image(links[count],uid[count])
                    news_beautification(part,news_tit[count],news_sentiment_score,news_sentiment_text,keyword_beautificaiton(keywords_list[count]),save_path,news_summary1[count],country[count],source[count])
                    count = count + 1
                st.write('----------------------------------------')
            except:
                continue
    
if __name__ == '__main__':
    news_main()