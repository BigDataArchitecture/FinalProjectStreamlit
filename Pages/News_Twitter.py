import streamlit as st
import Get_data
from helper import change,keyword_beautificaiton,get_image,clear_summary
from PIL import Image
from Twitter_Code import twitter_beautification

def news_main_twitter(country_selections,topic_selections):
    all_data = Get_data.filter_data(country_selections,topic_selections)
    def news_beautification(column,news_title,news_sentiment_score,news_sentiment_text,keywords,save_path,summary):
        image = Image.open(save_path)
        column.image(image,width=400)
        column.markdown('<div><p style="font-family:Times New Roman; color: '
        + change(news_sentiment_text, color = True)+'; font-size: 20px;">' 
        + change(news_sentiment_text, color = False) + " "+ news_sentiment_score + "%"  + '</p>'+ keywords + '<h4>'
        + news_title + '</h4><p style = "text-align: justify;text-justify: inter-word;">'+summary+'</div>'
        ,unsafe_allow_html=True)

    count = 1
    for data in all_data:
        try:
            if count == 10:
                break
            else:
                try:
                    m2,m3 = st.columns((3,5))
                    news_sentiment_score = str(round(data['news_sentiments'][0]['score']*100,2))
                    news_sentiment_text = data['news_sentiments'][0]['label']
                    save_path = get_image(data['news_top_image'],data['_id'])
                    if clear_summary(data['news_summary']):
                        summary = data['news_summary']
                    else:
                        continue
                    news_beautification(m2,data['news_title'],news_sentiment_score,news_sentiment_text,keyword_beautificaiton(data['news_keywords']),save_path, summary)
                    for j in range(min(len(data['news_tweets']),4)):
                        twitter_beautification(m3,data['news_tweets'][str(j)]['user']['displayname'],data['news_tweets'][str(j)]['user']['username'],data['news_tweets'][str(j)]['content'],data['news_tweets'][str(j)]['likeCount'],data['news_tweets'][str(j)]['retweetCount'],data['news_tweets'][str(j)]['user']['followersCount'],data['news_tweets'][str(j)]['user']['location'])
                    m2.markdown(f"<a href = '{data['news_link']}'>Read News</a>",unsafe_allow_html=True)
                    # if m2.button("Read Full Article",key = count): 
                    #     js = "window.open('" + data['news_link']+"')"  # New tab or window
                    #     # js = "window.location.href = '"+news_links[count]+"'" # Current tab
                    #     html = '<img src onerror="{}">'.format(js)
                    #     print(html)
                    #     div = Div(text=html)
                    #     st.bokeh_chart(div)
                    
                    st.write('----------------------------------------')
                    count = count + 1
                    print(count)
                except:
                    continue
        except:
            continue

if __name__ == '__main__':
    news_main_twitter()
