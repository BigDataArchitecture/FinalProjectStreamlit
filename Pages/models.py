import streamlit as st
import numpy as np
from pandas import DataFrame
from keybert import KeyBERT
from re import sub
import requests
from flair.embeddings import TransformerDocumentEmbeddings
import seaborn as sns
import os
import json
import spacy
from spacy_streamlit import visualize_ner
import ast
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, AutoModelForTokenClassification


def explore_models():

    def replace_fun(string1):
        newstring = string1.replace("<Pad>",'')
        newstring1 = newstring.replace("</S>",'')
        return newstring1

    def camel_case(s):
        s = sub(r"(_|-)+", " ", s).title()
        return s

    def _max_width_():
        max_width_str = f"max-width: 2000px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )


    _max_width_()

    c30, c31, c32 = st.columns([2.5, 1, 3])

    with c30:
        # st.image("logo.png", width=400)
        st.title("🔑 Explore our Models")
        st.header("")


    with st.expander("ℹ️ - About this app", expanded=True):

        st.write(
            """     
    -   This App lets you play with our models which are used in news aggregation we use 4 models 1) Summarization 2) Key word extraction 3) Sentiment Analysis 4) Name Entity of a document
    -   The *BERT Keyword Extractor* app is an easy-to-use interface built in Streamlit for the amazing [KeyBERT](https://github.com/MaartenGr/KeyBERT) library from Maarten Grootendorst!
    -   It uses a minimal keyword extraction technique that leverages multiple NLP embeddings and relies on [Transformers] (https://huggingface.co/transformers/) 🤗 to create keywords/keyphrases that are most similar to a document.
            """
        )

        st.markdown("")

    st.markdown("")
    st.markdown("## 📌 Paste document")
    with st.form(key="my_form"):
        ce, c1, ce, c2, c3 = st.columns([0.07, 1, 0.07, 5, 0.07])
        with c1:
            keyword = st.checkbox(
                "Keyword Extraction")
            sentiments = st.checkbox(
                "Sentiments")
            summary = st.checkbox(
                "Summary")
            NER = st.checkbox(
                "NER")
            
        with c2:
            doc = st.text_area(
                "Paste your text below (max 500 words)",
                height=510,
            )

            MAX_WORDS = 500
            import re
            res = len(re.findall(r"\w+", doc))
            if res > MAX_WORDS:
                st.warning(
                    "⚠️ Your text contains "
                    + str(res)
                    + " words."
                    + " Only the first 500 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
                )

                doc = doc[:MAX_WORDS]

            submit_button = st.form_submit_button(label="✨ Get me the data!")

    if not submit_button:
        st.stop()

    if keyword:
        # kw_model = KeyBERT(model=roberta)
        @st.cache(allow_output_mutation=True)
        def load_model():
            return  KeyBERT("distilbert-base-nli-mean-tokens")
        kw_model = load_model()
        keywords = kw_model.extract_keywords(
        doc,
        keyphrase_ngram_range=(1, 1),
        use_mmr=True,
        stop_words="english",
        top_n=10)

        st.markdown("## **Check results **")
        print(  )
        df = (
            DataFrame(keywords, columns=["Keyword/Keyphrase", "Relevancy"])
            .sort_values(by="Relevancy", ascending=False)
            .reset_index(drop=True)
        )
        df.index += 1

        # Add styling
        cmGreen = sns.light_palette("green", as_cmap=True)
        cmRed = sns.light_palette("red", as_cmap=True)
        df = df.style.background_gradient(
            cmap=cmGreen,
            subset=[
                "Relevancy",
            ],
        )
        c1, c2, c3 = st.columns([1, 3, 1])

        format_dictionary = {
            "Relevancy": "{:.1%}",
        }
        df = df.format(format_dictionary)
        with c2:
            st.table(df)

    if sentiments:
        tokenizer = AutoTokenizer.from_pretrained("finiteautomata/beto-sentiment-analysis",max_length=512)
        model = AutoModelForSequenceClassification.from_pretrained("finiteautomata/beto-sentiment-analysis")
        nlp = pipeline("sentiment-analysis", model = model, tokenizer=tokenizer)
        clean_text= doc.replace("\n", " ")       
        clean_text= ''.join([c for c in clean_text if c != "'"])
        sentiment = nlp(str(clean_text))
        st.write("Sentiments of this Doc is ",sentiment[0]['label']," with ", str(sentiment[0]['score']), "score")

    if summary:
        url = 'https://yto0kae7xb.execute-api.us-east-1.amazonaws.com/dev/qa'
        event = {"context": doc}
        print(event)
        response = requests.post(url,json=event)
        output = response.content.decode()
        an = json.loads(output)
        print(an)
        stripped_string = replace_fun(an['answer'])
        stripped_string = camel_case(an['answer'])
        st.write(stripped_string)
    if NER:
        def load_model(name: str) -> spacy.language.Language:
            """Load a spaCy model."""
            return spacy.load(name)
        entity_list = []
        def NLP_NER_OUTPUT(event):
            url = 'https://0rwjoafjn8.execute-api.us-east-1.amazonaws.com/dev/qa'
            response1 = requests.post(url,json=event)
            output1 = response1.content.decode()
            an1 = json.loads(output1)
            print(an1)
            try:
                a1 = an1['answer']
                b = str(a1)
                Final_dict = ''
                list_b = list(b)
                for i in range(1,len(list_b)-1):
                    Final_dict = Final_dict +list_b[i]
                es = ast.literal_eval(Final_dict)
                return es
            except:
                return 1
        nlp = load_model("en_core_web_sm")
        doc = nlp(doc)
        visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
        print(visualize_ner)
        # nlp = spacy.load("en_core_web_lg")
        # text = nlp(doc)
        # event = {"context": doc}
        # for entity in text.ents:
        #     st.write(entity.text, entity.label_)
        # output_dict = NLP_NER_OUTPUT(event)
        # print(output_dict)
        # if output_dict == 1:
        #     st.write('Nothing found for NER')
        # else:
        #     for i in range(len(output_dict)):
        #         if output_dict[i]['score'] > 0.99:
        #             print(output_dict[i]['entity'])
        #             print(output_dict[i]['word'])
        #             entity_list.append(output_dict[i]['word'])
        #             print(entity_list)
        # st.title("Entities Identified")
        # st.write(entity_list)

            


if __name__ == '__main__':
    explore_models()    
