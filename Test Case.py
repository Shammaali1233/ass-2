# Test Case
# test_museum.py
import unittest
from Location import Location
from Artwork import Artwork
from Event import Event
from Visitor import Visitor
from Guide import Guide
from Ticket import Ticket

class TestMuseum(unittest.TestCase):

    def setUp(self):
        self.location = Location('Exhibition Hall A')
        self.artwork = Artwork('Mona Lisa', 'Leonardo da Vinci', '1503', 'Renaissance art', self.location)
        self.event = Event('Exhibition', self.location)
        self.visitor = Visitor('John Doe', 30, '123456')
        self.guide = Guide('Jane Smith', '987654')

    def test_add_new_artwork(self):
        new_artwork = Artwork('The Starry Night', 'Vincent van Gogh', '1889', 'Post-Impressionism', self.location)
        self.location.add_artwork(new_artwork)
        self.assertIn(new_artwork, self.location.artworks)

    def test_open_new_exhibition(self):
        new_event = Event('Impressionism Exhibition', self.location)
        self.location.add_event(new_event)
        self.assertIn(new_event, self.location.events)

    def test_purchase_ticket(self):
        self.visitor.buy_ticket(self.event)
        self.assertEqual(len(self.visitor.tickets), 1)
        self.assertIsInstance(self.visitor.tickets[0], Ticket)
        self.assertEqual(self.visitor.tickets[0].event, self.event)

    def test_display_payment_receipt(self):
        self.visitor.buy_ticket(self.event)
        receipt = self.visitor.tickets[0].get_receipt()
        self.assertIn('John Doe', receipt)
        self.assertIn('Exhibition', receipt)
        self.assertIn('Exhibition Hall A', receipt)

if _name_ == '_main_':
    unittest.main()