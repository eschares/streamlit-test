# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:08:46 2021

@author: eschares
"""

import streamlit as st
import pandas as pd
import numpy as np
    
st.title('Elsevier 2021 Cancellations')
st.write("Here's our first attempt at using data to create a table:")

file = "Unsub_Elsevier_2021_cancellations.csv"
df = pd.read_csv(file)
st.write(df.head())

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['subscribed'].unique())

'You selected: ', option

slide = st.sidebar.slider(
    'How much OA?',
    min(df['free_instant_usage_percent']),
    max(df['free_instant_usage_percent']),
    )