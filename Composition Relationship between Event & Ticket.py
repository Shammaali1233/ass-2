# Composition Relationship between Event & Ticket
class Event:
    def _init_(self, name, location):
        self.name = name
        self.location = location
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)  # This is where the composition is established


class Ticket:
    def _init_(self, visitor, event):
        self.visitor = visitor
        self.event = event  # This is where the composition is established
        event.add_ticket(self)  # A ticket cannot exist without an event
