import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from PIL import Image

img = Image.open('final.jpg')
st.set_page_config(page_title='Spam Detector', page_icon=img)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.markdown("<h1 style='text-align: center; color: white;'>Email/SMS Spam Detector</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>Made By - Raihan Khan</h1>", unsafe_allow_html=True)

input_sms = st.text_area("Enter the message.")
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('PREDICT')
if center_button:

    transformed_sms = transform_text(input_sms)
 
    vector_input = tfidf.transform([transformed_sms])
  
    result = model.predict(vector_input)[0]
    
    if result == 1:
        st.markdown("<h1 style='text-align: center; color: red;'>Spam</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; color: white;'>Not Spam</h1>", unsafe_allow_html=True)
#CODE BY - RAIHAN KHAN