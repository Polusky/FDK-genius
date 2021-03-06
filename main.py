import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk


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

st.title("Malaysian Covid-19 Statistics.")
st.subheader("Data shown:")

col1, col2, col3, col4, col5, col6, col7, col8 = st.beta_columns(np.ones(8))

if (col1.button("Cases")):
    datatoshow = 1
if (col2.button("Deaths")):
    datatoshow = 2

# data processing
try:
    if (datatoshow == 2):
        data_file = open("testdeaths.csv")
    else:
        data_file = open("testcases.csv")
except NameError:
    "Please select a dataset."
    st.stop()

if (datatoshow == 2):
    hexacolor = [[237, 248, 251], [191, 211, 230],
                 [158, 188, 218], [140, 150, 198], [136, 86, 167], [129, 15, 124]]
else:
    hexacolor = [[255, 255, 178], [254, 217, 118],
                 [254, 178, 76], [253, 141, 60], [240, 59, 32], [189, 0, 38]]
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
                          colorRange=hexacolor,
                          extruded=True,
                          elevation_range=[0, 5000]
                          )
                ]
    ))))
