import pymongo
import streamlit as st


def access_data():
    client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
    print(client["News"])
    db = client["News"]
    collection = db["GoogleAPI"]
    all_data = collection.find()
    return all_data

def column_specific_data(columnname):
    list1 = []
    client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
    db = client["News"]
    collection = db["GoogleAPI_links"]
    all_data = collection.find({},{'_id': 0, columnname: 1})
    for i in all_data:
        list1.append(i[columnname])
    return list(set(list1))

# def filter_data_country(country_selections):
#     print(country_selections)
#     myquery = {"news_Country": country_selections[-1]}
#     client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
#     print(client["News"])
#     db = client["News"]
#     collection = db["GoogleAPI"]
#     mydoc = collection.find(myquery)
#     return mydoc

# def filter_data_topic(topic_selection):
#     myquery = {"news_topic": topic_selection[-1]}
#     client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
#     print(client["News"])
#     db = client["News"]
#     collection = db["GoogleAPI"]
#     mydoc = collection.find(myquery)
#     return mydoc

def filter_data(country_selections,topic_selection):
    myquery = {"news_Country": {"$in": country_selections}, "news_topic":  {"$in": topic_selection}}
    print(myquery)
    client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
    print(client["News"])
    db = client["News"]
    collection = db["GoogleAPI_links"]
    mydoc = collection.find(myquery)
    return mydoc
