# Association Relationship between Artwork & Location
class Artwork:
    def _init_(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location  # This is where the association is established


class Location:
    def _init_(self, name):
        self.name = name
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        artwork.location = self  # This is where the association is established
