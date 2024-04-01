# Inheritance Relationship between Ticket and Visitor
class Ticket:
    def _init_(self, visitor, price):
        self.visitor = visitor
        self.price = price


class ExhibitionTicket(Ticket):
    def _init_(self, visitor):
        super()._init_(visitor, price=20)  # Assuming the price for an ExhibitionTicket is 20


class TourTicket(Ticket):
    def _init_(self, visitor):
        super()._init_(visitor, price=30)  # Assuming the price for a TourTicket is 30


class SpecialEventTicket(Ticket):
    def _init_(self, visitor):
        super()._init_(visitor, price=50)  # Assuming the price for a SpecialEventTicket is 50
