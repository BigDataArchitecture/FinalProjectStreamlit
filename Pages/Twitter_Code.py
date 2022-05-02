import pymongo
import streamlit as st
import Get_data


from bokeh.models.widgets import Div
# st.set_page_config(
#     page_title="Twiiter",
#     page_icon="🎈",
#     layout="wide"
# )

# if st.button('Go to Streamlit'):
#     js = "window.open('https://twitter.com/chrisfos72')"  # New tab or window
#     # js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
#     html = '<img src onerror="{}">'.format(js)
#     div = Div(text=html)
#     st.bokeh_chart(div)

# # link = '[GitHub](http://github.com)'
# # st.markdown(link, unsafe_allow_html=True)

#Call the data 
all_data = Get_data.access_data()


def twitter_beautification(column,name,username,content,likeCount,retweet,followersCount,location):
    column.markdown('<style> .intro{box-shadow: 6px 6px 29px -4px rgba(0, 0, 0, 0.75); border-radius: 5px;border: 3px solid #1DA1F2; padding: 10px; margin: 20px; background: linear-gradient(to bottom, #66ccff -100%, #ccffff 100%);}</style><div class="intro"><h5><img src="https://img.icons8.com/fluency/30/000000/twitter.png"/>'
     + name + 
    '<img src="https://img.icons8.com/material-outlined/24/000000/email.png"/>'
     + username + '&emsp;&emsp;' + str(followersCount) + ' Followers ' + location + 
     '</h5> <a><span>' + content + 
     '</span><br><img src="https://img.icons8.com/external-those-icons-lineal-those-icons/24/000000/external-like-touch-gestures-those-icons-lineal-those-icons.png"/>&emsp;'
     + str(likeCount) + '&emsp;&emsp;' + 
     '<img src="https://img.icons8.com/material-outlined/24/000000/retweet.png"/>&emsp;' + str(retweet) + 
     '<br></div>',unsafe_allow_html=True)

count = 1
for data in all_data:
    if count == 10:
        break
    else:
        try:
            twitter_beautification(data['news_tweets'][str(count)]['user']['displayname'],data['news_tweets'][str(count)]['user']['username'],data['news_tweets'][str(count)]['content'],data['news_tweets'][str(count)]['likeCount'],data['news_tweets'][str(count)]['retweetCount'],data['news_tweets'][str(count)]['user']['followersCount'],data['news_tweets'][str(count)]['user']['location'])
            count = count + 1
        except:
            continue
        # st.markdown("""<iframe width="120" src="https://twitter.com/johnebhome/status/1520131611110563840"></iframe>""", unsafe_allow_html=True)
