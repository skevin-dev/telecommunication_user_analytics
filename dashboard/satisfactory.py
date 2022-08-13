import streamlit as st
import pandas as pd

def app():
    st.title('User Satisfaction page')

    st.markdown('**This is the `User Satisfaction` of this the user analysis multi page.**')

    st.markdown('**In this app, we will see the data of satisfactory analysis.**')

    df = pd.read_csv('./data/satsf.csv')
    st.write(df)