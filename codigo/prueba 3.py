import folium
from geopy import Nominatim
from folium.plugins import MiniMap
import folium
import osmapi
user = 'anto4nt0'
password = '18carolina'

# Crear un cliente de OSM autenticado
client = osmapi.OsmApi(username=user, password=password)

# Coordenadas de origen y destino
origen = (-71.5945098234529,-33.035801181260815)  
destino = (-71.59429091050319,-33.036093822867834)  


# Obtener la ruta entre origen y destino
route = client.(origen, destino)

# Crear un mapa con las coordenadas del origen
edificioC= folium.Map(location=[-33.03598990, -71.5946348], zoom_start=18) 
# Añadir marcadores para el origen y el destino
folium.Marker(location=origen, popup='Origen').add_to(edificioC)
folium.Marker(location=destino, popup='Destino').add_to(edificioC)

# Añadir una línea para cada segmento de la ruta
for segment in route:
    coordinates = [(node['lat'], node['lon']) for node in segment['geometry']]
    folium.PolyLine(locations=coordinates, color='blue', weight=2.5, opacity=1).add_to(edificioC)
edificioC

