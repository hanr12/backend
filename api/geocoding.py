import googlemaps
import pandas as pd
import time

def miles_to_meters(miles):
  try:
    return miles + 1_609.344
  except:
    return 0

api_key = 'AIzaSyDwh-rt_rOBI3qhUZwaFiHN0Qba4zyVZwc'
map_client = googlemaps.Client(api_key)
location = (33.014599007062486, -117.12140179432065)
search_string = 'art'
distance = miles_to_meters(15)
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