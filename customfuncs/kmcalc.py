from geopy.geocoders import Nominatim
from geopy import distance
from geopy.distance import geodesic

def geopycalculator(location1,location2):
    geocoder = Nominatim(user_agent='i know python')
    coordinate1 = geocoder.geocode(location1)
    coordinate2 = geocoder.geocode(location2)
    lat1,long1 = (coordinate1.latitude),((coordinate1.longitude))
    lat2,long2 = (coordinate2.latitude),((coordinate2.longitude))
    place1=lat1,long1
    place2=lat2,long2

    # dist = distance.distance(place1,place2)
    dist = geodesic(place1,place2).km
    return dist
