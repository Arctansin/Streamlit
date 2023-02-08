#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="DataFrame Formatting", page_icon="📊")

with open("/Users/mingming/Desktop/Streamlit/pages/style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

df = pd.DataFrame(
   np.random.randn(10, 20),
   columns=('col %d' % i for i in range(20)))



st.markdown("# DataFrame Format")
st.sidebar.header("DataFrame Format")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)

def format_color_groups(df):
    colors = ['gold', 'lightblue']
    x = df.copy()
    factors = list(x['col 0'].unique())
    i = 0
    for factor in factors:
        style = f'background-color: {colors[i]}'
        x.loc[x['col 0'] == factor, :] = style
        i = not i
    return x



st.dataframe(df.style.apply(format_color_groups, axis=None))