import folium.map
import openrouteservice
from openrouteservice import directions
import folium

client = openrouteservice.Client(key='5b3ce3597851110001cf62480b49af1d643e403db958615a7b918bc2')
edificioC= folium.Map(location=list(reversed([ -71.5946348,-33.03598990])), zoom_start=20)
coords= ((-71.59453432716008,-33.0362753034251),(-71.59433741564055,-33.035740215344255))
route= directions(client,coords)
folium.PolyLine(locations=[list(reversed(coords)) for coords in route['features'][0]('geometry')],color='blue').add_to(edificioC)
edificioC
