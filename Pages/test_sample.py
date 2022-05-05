# content of test_sample.py
from helper import change,keyword_beautificaiton,get_image,clear_summary
from Get_data import access_data,filter_data

#Test 1 to test color
def test_change_function():
    a = change("POS")
    assert(a == 'Green')
    a = change("positive")
    assert(a == 'Green')
    a = change("NEG")
    assert(a == 'Red')
    a = change("NEG")
    assert(a == 'Red')
    a = change("NEU")
    assert(a == 'Blue')
    a = change("neutral")
    assert(a == 'Blue')

#Test 2 to test Full form
def test_change_function_name():
    a = change("POS",color= False)
    assert(a == 'Positive')
    a = change("positive",color= False)
    assert(a == 'Positive')
    a = change("NEG",color= False)
    assert(a == 'Negative')
    a = change("NEG",color= False)
    assert(a == 'Negative')
    a = change("NEU",color= False)
    assert(a == 'Neutral')
    a = change("neutral",color= False)
    assert(a == 'Neutral')

def test_keyword():
    a = keyword_beautificaiton(['Text1','Text2'])
    assert(a == "No Keyword")
    lis = ['Text1','Text2','Text3','Text4']
    a = keyword_beautificaiton(lis)
    assert(a == ' TEXT1 TEXT2 TEXT3 TEXT4')


def test_get_image():
    save_path = get_image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dreamstime.com%2Fphotos-images%2Flove.html&psig=AOvVaw10CMmn0PZZyP5HSLWcZmLY&ust=1651813049741000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCPjWoKLJx_cCFQAAAAAdAAAAABAJ","1")
    assert(save_path == "1.png")

def test_clean_summary():
    a = clear_summary("12345678901234567")
    assert(a==False)
    a = clear_summary("1234567890")
    assert(a==True)
    a = clear_summary("1234 1234 1234")
    assert(a==True)

def test_access_data():
    data = access_data()
    counter = 0
    for i in data:
        if counter > 0:
            break
        else:
            counter = counter + 1
    assert(counter > 0)

def test_column():
    data = filter_data("Australia","Business")
    counter = 0
    for i in data:
        if counter > 0:
            break
        else:
            counter = counter + 1
    assert(counter > 0)

