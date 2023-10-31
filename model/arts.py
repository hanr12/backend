from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artwork(db.Model):
    """
    Model for artworks.
    """
    __tablename__ = 'artworks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist_display = db.Column(db.String(255), nullable=False)
    date_display = db.Column(db.String(255))
    medium_display = db.Column(db.String(255))
    dimensions = db.Column(db.String(255))
    image_id = db.Column(db.Integer)
    image_url = db.Column(db.String(255))
    # Add more fields as needed

    def __init__(self, title, artist_display, date_display=None, medium_display=None, dimensions=None, image_id=None, image_url=None):
        self.title = title
        self.artist_display = artist_display
        self.date_display = date_display
        self.medium_display = medium_display
        self.dimensions = dimensions
        self.image_id = image_id
        self.image_url = image_url

    def as_dict(self):
        """
        Return the object as a dictionary.
        """
        return {
    "data": {
        "id": 129884,
        "title": "Mona Lisa",
        "artist_display": "Leonardo da Vinci",
        "date_display": "c. 1503-1506",
        "medium_display": "Oil on panel",
        "dimensions": "30 x 20 in. (77 x 53 cm)",
        "image_id": 121896,
        "image_url": "https://www.artic.edu/iiif/2/8c32b8a1-1fe0-4ee3-8e1e-bd97d98ed156/full/400,/0/default.jpg"
        }
    }
