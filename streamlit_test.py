# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:08:46 2021

@author: eschares
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
    
st.title('Streamlit modules')
st.write("Here's our first attempt at using data to create a table:")

file = "Unsub_Elsevier_2021_cancellations.csv"
df = pd.read_csv(file)
df

#dropdown select box
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['subscribed'].unique())     #FALSE MAYBE TRUE BLANK
'You selected: ', option

#Line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.sidebar.line_chart(chart_data)

#map data enabled with checkbox
if st.sidebar.checkbox('Show map of San Francisco'):
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_data)
    

slide = st.sidebar.slider(
    'How much OA?',
    min(df['free_instant_usage_percent']),
    max(df['free_instant_usage_percent']),
    )

left_column, right_column = st.beta_columns(2)
if left_column.button('Enable a...'):
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

if (0):
    #Progress bar
    'Starting a long computation...'
    
    
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i + 1)
      time.sleep(0.05)
    
    '...and now we\'re done!'



st.button('Button click me')
st.checkbox('Checkbox Check me out')
radiovalue = st.radio('Radio', [1,2,3])
'You picked ', radiovalue
st.selectbox('Selectbox', [1,2,3])
st.multiselect('Multiselect', ['A','B','C'])
st.slider('Slider', min_value=0, max_value=100)
st.select_slider('Select slider individual options', options=[1,20,'test','bob'])
st.text_input('Text input')
st.number_input('Number input')
st.text_area('Text area')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.color_picker('Pick a color')
