import folium
from folium import plugins
import pandas as pd
import os
import json
import ipywidgets
from geopy.geocoders import nominatim


EdificioCLOC= (-33.036018, -71.594655)
map_edificioC= folium.Map(location=EdificioCLOC, width= '75%', zoom_start =18)

testgeo= ''
def switchPosition(coordinate):
    temp= coordinate[0]
    coordinate[0]= coordinate[1]
    coordinate[1]= temp
    return coordinate



map_edificioC
