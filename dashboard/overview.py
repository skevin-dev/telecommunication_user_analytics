import streamlit as st
import pandas as pd

def app():
    st.title('the User Overview page')

    st.markdown('**This is the `User Overview` of this the user analysis multi page.**')

    st.markdown('**In this app, we will see the data and some visualization of user engagement.**')

    st.title('Total data for each application')
    st.image('https://i.ibb.co/bBPFDJV/download.png')
    st.title('Correlation of data')
    st.image('https://i.ibb.co/jzRwhPX/download-1.png')