import requests

def change(keyword, color = True):
    if color:
        if keyword == 'NEU' or keyword == 'neutral':
            return 'Blue'
        if keyword == 'NEG' or keyword == 'negative':
            return 'Red'
        if keyword == 'POS' or keyword == 'positive':
            return 'Green'
    else:
        if keyword == 'NEU' or keyword == 'neutral':
            return 'Neutral'
        if keyword == 'NEG' or keyword == 'negative':
            return 'Negative'
        if keyword == 'POS' or keyword == 'positive':
            return 'Positive'

def keyword_beautificaiton(list1):
    try:
        concat =  ""
        for i in range(4):
            concat = concat + " " + list1[i].upper()
        return concat
    except:
        return "No Keyword"


def get_image(link,uid):
    print("pathhh")
    response = requests.get(link)
    save_path = (str(uid)+".png")
    print("pathhh")
    file = open(save_path, "wb")
    file.write(response.content)
    file.close()
    print("saved")
    return save_path


def convert(lst):
    return (lst[0].split())

def clear_summary(text):
    list1 = text.split()
    for i in list1:
        if len(str(i)) > 15:
            return False
        else:
            continue
    return True
