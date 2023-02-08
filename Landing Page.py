#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:04:57 2023

@author: mingming
"""
import streamlit as st
from streamlit_card import card

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

with open("style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    
    
st.write("# Welcome to Streamlit! 👋")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

from PIL import Image
background=Image.open("background1.jpg")
st.image(background)

from streamlit_extras.switch_page_button import switch_page
col1,col2=st.columns(2)
with col1:
    DataFrame_Page=card(
        title="Go to x1 demo",
        text="this is for x1 demoss",
        image="http://localhost:8501/media/b09ca6a072c8a337899c4bf69d2bb136f53e7c983b677a916a381f94.jpg",
        key="card 1"
        )
    if DataFrame_Page:
        switch_page("Plotting Demo")
with col2:
    DataFrame_Page=card(
        title="Go to x2 demo",
        text="this is for x2 demoss",
        image="http://localhost:8501/media/b09ca6a072c8a337899c4bf69d2bb136f53e7c983b677a916a381f94.jpg",
        key="card 2"
        )
    if DataFrame_Page:
        switch_page("Mapping Demo")






