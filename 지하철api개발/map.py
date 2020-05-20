import folium

map = folium.Map(location=[37.564214, 127.001699],
               tiles="OpenStreetMap",
              zoom_start=15)

folium.Marker(
    location=[37.564214, 127.001699],
    popup="Marker Here",
    icon=folium.Icon(icon='green')
).add_to(map)
map.save('map.html')

