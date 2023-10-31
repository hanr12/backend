from flask import Blueprint, jsonify 
from flask_restful import Api, Resource 
import googlemaps
import pandas as pd
import time

from model.geocoding import *

geocoding_api = Blueprint('geocoding_api', __name__,
                   url_prefix='/api/geocoding')

api = Api(geocoding_api)

api_key = 'AIzaSyDwh-rt_rOBI3qhUZwaFiHN0Qba4zyVZwc'
map_client = googlemaps.Client(api_key)

class GeocodingApi:
  class _Create(Resource):
        def post(self, art_museum):
            pass
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getArtmuseum())
          
 class _ReadID(Resource):
        def get(self, id):
            return jsonify(getArtmuseum(id))
  
location = (33.014599007062486, -117.12140179432065)
search_string = 'art'
business_list = []
response = map_client.places_nearby(
  Location=location,
  keyword=search_string,
  name='art museum',
  radius=distance,
)
business_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')
while next_page_token:
  time.sleep(2)
  response = map_client.places_nearby(
    Location=location,
    keyword=search_string,
    name='art museum',
    radius=distance,
    page_taken=next_page_token
  )
  business_list.extend(response.get('results'))
  next_page_token = response.get('next_page_token')
df = pd.DataFrame(business_list)
df['url'] = 'https://www.google.com/maps/place?q=place_id' + df['place_id']
df.to_excel('art museum list.xlsx',index=False)