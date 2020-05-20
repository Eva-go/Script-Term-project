import folium


pointX=430
pointY=2300
map = folium.Map(location=[pointX, pointY],
               tiles="OpenStreetMap",
              zoom_start=15)

folium.Marker(
    location=[pointX, pointY],
    popup="Marker Here",
    icon=folium.Icon(icon='green')
).add_to(map)
map.save('map.html')

