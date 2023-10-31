import googlemaps
import prettyprint
import requests

def searchplace():

    api_key = 'AIzaSyBI4Al2OvpqZBQeHCB0pAgrz08ilFCAB4A'
    map_client = googlemaps.Client(api_key)
    search_string = "art museums"

    #code - establish current location
 #    currentloc = googlemaps.LatLng(33.00353564831884,-117.13532743795295)
    response = map_client.places(query=search_string)
    results = response.get('results')[0]
    return results
