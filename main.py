import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import urllib.request

# Coordinates for hexagon centers.
coordict = {"WP Kuala Lumpur": [101.688021, 3.137766],
            "Selangor": [101.490152, 3.393868],
            "WP Putrajaya": [101.689633, 2.935041],
            "Perlis": [100.251344, 6.471045],
            "Kedah": [100.718819, 5.899533],
            "Pulau Pinang": [100.245534, 5.395335],
            "Perak": [101.097147, 4.608176],
            "Kelantan": [102.065872, 5.353022],
            "Terengganu": [103.008063, 4.971741],
            "Pahang": [102.571229, 3.724446],
            "Negeri Sembilan": [102.241698, 2.729081],
            "Melaka": [102.319400, 2.319983],
            "Johor": [103.444895, 2.014039],
            "Sarawak": [113.839051, 2.473882],
            "Sabah": [117.020172, 5.222607],
            "WP Labuan": [115.222279, 5.311390]}

# initial data processing
data_file = open("testdata.csv")
data_raw = data_file.readlines()

data = []
df = []

for lines in data_raw:
    data.append(lines.split(","))

for count in data:
    for i in range(int(count[1])):
        df.append(coordict[count[0]])


st.pydeck_chart(pdk.Deck(
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=5,
            longitude=108.5,
            zoom=4.5,
            pitch=50,
        ),
        layers=[pdk.Layer(type='HexagonLayer',
                          data=df,
                          get_position='-',
                          auto_highlight=True,
                          elevation_scale=100,
                          radius=15000,
                          pickable=True,
                          extruded=True,
                          elevation_range=[0, 5000]
                          )
                ]
    ))))
