from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import requests
import random


def get_artworks():
    api_url = 'https://api.artic.edu/api/v1/artworks'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []


artworks_api = Blueprint('artworks_api', __name__, url_prefix='/api/artworks')
api = Api(artworks_api)

class ArtworksAPI(Resource):
    def get(self):
        return jsonify(get_artworks())

api.add_resource(ArtworksAPI, '/')

if __name__ == "__main__":
    server = 'https://flask.nighthawkcodingsociety.com'
    url = server + "/api/artworks"
    responses = []

    responses.append(requests.get(url))

    for response in responses:
        print(response)
        try:
            print(response.json())
        except Exception as e:
            print(f"Error: {e}")
