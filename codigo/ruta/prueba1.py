import openrouteservice as ors
import folium

client = ors.Client(key='5b3ce3597851110001cf62480b49af1d643e403db958615a7b918bc2')
m = folium.Map(location=[-71.59075,-33.03338], tiles='cartodbpositron', zoom_start=13)

# Some coordinates in Berlin
coordinates = [[-71.59074425697328, -33.0331231495204],[-71.59074425697328, -33.0331231495204]]

route = client.directions(
    coordinates=coordinates,
    profile='foot-walking',
    format='geojson',
    options={"avoid_features": ["steps"]},
    validate=False,
)
folium.PolyLine(locations=[list(reversed(coord)) 
                           for coord in 
                           route['features'][0]['geometry']['coordinates']]).add_to(m)
    
m
