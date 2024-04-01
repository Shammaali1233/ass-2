# Association Relationship between Event and Location
class Event:
    def _init_(self, name, location):
        self.name = name
        self.location = location  # This is where the association is established



class Location:
    def _init_(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        event.location = self  # This is where the association is established
