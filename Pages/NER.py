import json
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, AutoConfig
import pymongo
import spacy

def NER_keywrod(sentence):
    entity_list = ['EVENT','GPE', 'MONEY', 'ORG','PERSON', 'PRODUCT', 'QUANTITY', 'TIME']
    def show_ents(doc):
        list_keywords = ""
        if doc.ents:
            for ent in doc.ents:
                if str(ent.label_) in entity_list:
                    list_keywords = list_keywords + ent.text
            return list_keywords
        else:
            print('No named entities found.')
            return list_keywords
            
    nlp = spacy.load('en_core_web_sm-3.0.0')
    doc = nlp(sentence)
    list_keywords =  show_ents(doc)
    return list_keywords
