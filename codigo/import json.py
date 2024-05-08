import json
import folium
from geopy import Nominatim
from folium.plugins import MiniMap
import pyroute2 
popuptext= '<b>Edificio C</B>'
edificioC= folium.Map(location=[-33.03598990, -71.5946348], zoom_start=20) 
folium.Marker(location=[-33.03598990, -71.5946348],popup=popuptext).add_to(edificioC)
edificioC

