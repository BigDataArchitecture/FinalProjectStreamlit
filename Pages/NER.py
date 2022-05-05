import json
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig
import pymongo
import spacy

list_keywords = []
entity_list = ['EVENT','GPE', 'MONEY', 'ORG','PERSON', 'PRODUCT', 'QUANTITY', 'TIME']
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            if str(ent.label_) in entity_list:
                list_keywords.append(ent.text)
                print(ent.text+'-'+str(ent. start_char)+'-'+str(ent.label_))
    else:
        print('No named entities found.')

nlp = spacy.load("en_core_web_sm")
doc = nlp("How is Ukraine doing this days?")
labels=nlp.get_pipe("ner")
print(show_ents(doc))
print(list_keywords)
