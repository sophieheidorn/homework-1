# SETUP
import streamlit as st

import numpy as np
import pandas as pd
import altair as alt

from pathlib import Path
import datetime as dt
from datetime import datetime

#-------------------
# DATA

# Data import
df = pd.read_csv("https://github.com/sophieheidorn/homework-1/blob/main/data/external/data.csv", on_bad_lines='skip')

# Data transformation
df['Date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')



#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Make a chart_party 
chart_party = st.sidebar.multiselect('Select party', df['party'].unique().tolist())

# Create a subset out of chart_party 
if len(chart_party) > 0:
    df_subset = df[df['party'].isin(chart_party)]
    

#-------------------
# HEADER

# Title of our app
st.title("Count of party members questioned ")
# Add header
st.header("This is the interactive app from team G")

#-------------------
# BODY

#-------------------
# Show static DataFrame
st.subheader("Show Data")
st.write("Here's my data:")
chart = alt.Chart(df).mark_bar(size = 40).encode(
    x=alt.X('party',
            sort='-y',
            axis=alt.Axis(title="Party", 
                          titleAnchor="middle", 
                          labelAngle=0)),
    y=alt.Y('count(party)', 
            axis=alt.Axis(title = "Count", 
                          titleAnchor="middle")),
    color=alt.Color('party', scale=alt.Scale(scheme='pastel2'))
).properties(
    title='Count of party members questioned ',
    width=350,
    height=250
).configure_title(
    fontSize=15,
    font='Arial',
    anchor='middle',
    color='black'
)

chart
#-------------------
# Show a map
st.write("Plot a map")
st.map(df_subset)

#-------------------