# Dependency Relationship between Guide and Event
class Guide:
    def _init_(self, name):
        self.name = name
        self.events = []

    def facilitate_event(self, event):
        self.events.append(event)  # This is where the dependency is established
        event.guide = self  # An event depends on a guide for its facilitation


class Event:
    def _init_(self, name, location):
        self.name = name
        self.location = location
        self.guide = None  # This will be set when a guide facilitates the event
