import streamlit as st
import pickle
import pandas as pd
import numpy as np
import base64

wine_predict = pickle.load(open('Wine_Price_Ml.pkl', 'rb'))
wine_data = pd.read_csv('wine_file.csv')

st.set_page_config(page_title="Wine Price Prediction App", layout="wide")

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.css-1j6homm e1tzin5v0{
margin: 1px;
}
</style> """, unsafe_allow_html=True)


# Change background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('wine.jpg')

custom_css = """
<style>
.css-18e3th9 {
  padding-top: 1px;
  padding-bottom: 0px;
  
}
</style>
"""

# Call st.markdown() with the custom CSS style
st.markdown(custom_css, unsafe_allow_html=True)

col1, col2 = st.columns([1.1, 1.1])
with col1:
    st.title('Wine price prediction')

    var1 = st.selectbox('Variety', wine_data['variety'].unique())
    wine1 = st.selectbox('Winery', wine_data['winery'].unique())
    con = st.selectbox('Country', wine_data['country'].unique())
    pro = st.selectbox('Provience', wine_data['province'].unique())
    pts = st.selectbox('Raitings', sorted(wine_data['points'].unique()))

if st.button('Predict Price'):
    prediction = wine_predict.predict(pd.DataFrame(columns=['winery', 'variety', 'country', 'province', 'points'],
                                                   data=np.array([wine1, var1, con, pro, pts, ]).reshape(1, 5)))
    st.text("Estimated price : $" + str(np.round(prediction[0], 2)))
