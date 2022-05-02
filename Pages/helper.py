import requests

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
