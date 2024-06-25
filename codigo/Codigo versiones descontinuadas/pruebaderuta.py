import folium
import pyproj
import requests
from openrouteservice import client
from shapely.geometry import Point, LineString, Polygon, MultiPolygon
from shapely import wkt, geometry
api_key = '5b3ce3597851110001cf62480b49af1d643e403db958615a7b918bc2'
ors = client.Client(key=api_key)  # Create client with api key
 
edificioC = folium.Map(location=[-33.03601615746277,-71.59457966114627], zoom_start=18.49)
edificioC

def style_function(color):
    return lambda feature: dict(color=color,
                                weight=3,
                                opacity=0.5)

map_params = {'tiles': 'Edificio C',
              'location': ([-33.03601615746277,-71.59457966114627]),
              'zoom_start': 18.49}
# Request normal route between appropriate locations without construction sites
request_params = {'coordinates': [[-33.03626295319385,-71.59453761918188],
                                  [-33.035740215344255,-71.59433741564055]],
                  'format_out': 'geojson',
                  'profile': 'foot-walking',
                  'preference': 'shortest',
                  'instructions': 'false', }
route_normal = ors.directions(**request_params)
folium.features.GeoJson(data=route_normal,
                        name='camino',
                        style_function=style_function('#FF0000'),
                        overlay=True).add_to(map_params)



map2