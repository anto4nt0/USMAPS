import folium
import requests

# Coordenadas de origen y destino (ejemplo)
origen = (-71.5945098234529,-33.035801181260815)  
destino = (-71.59429091050319,-33.036093822867834)  

# Parámetros para la solicitud al servicio de enrutamiento de OpenRouteService
parameters = {
    'coordinates': f"{origen[1]},{origen[0]}|{destino[1]},{destino[0]}",
    'profile': 'foot-walking',  # Perfil de enrutamiento: coche
    'format': 'geojson',  # Formato de respuesta: JSON
}

# Hacer la solicitud al servicio de enrutamiento de OpenRouteService
response = requests.get('https://api.openrouteservice.org/v2/directions/foot-walking?api_key=5b3ce3597851110001cf62480b49af1d643e403db958615a7b918bc2&start=-71.5945098234529,-33.035801181260815&end=-71.59429091050319,-33.036093822867834', params=parameters)

# Obtener la respuesta en formato JSON
data = response.json()

# Crear un mapa con las coordenadas del origen
edificioC= folium.Map(location=[-33.03598990, -71.5946348], zoom_start=18) 

# Añadir marcadores para el origen y el destino
folium.Marker(location=origen, popup='Origen').add_to(edificioC)
folium.Marker(location=destino, popup='Destino').add_to(edificioC)

# Añadir una línea para la ruta obtenida
route_geometry = data['features'][0]['geometry']['coordinates']
folium.PolyLine(locations=route_geometry, color='blue', weight=2.5, opacity=1).add_to(edificioC)

# Guardar el mapa como un archivo HTML
edificioC.save("ruta.html")