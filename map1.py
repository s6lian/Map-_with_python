import folium
import pandas
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<= elevation <3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location =[38.58, -99.09], zoom_start = 6, tiles = "Mapbox Bright")
#create a feature group

# add  point marker to the Map
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, ev in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location= [lt,ln], popup=folium.Popup(str(ev)+" m", parse_html= True), color=color_producer(ev), fill= True, fill_opacity = 0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),
style_function=lambda x: {'color':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties'] ['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
# LayerControl looks for  all the child that added to the map

map.save("Map.html")
