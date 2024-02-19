"""
test_hotel.py - Script that makes a unity test for the hotel functions
"""

# !/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the libraries needed
import unittest
import os
from hotel import Hotel

# In[2]:
class TestHotel(unittest.TestCase):
    """
    Test case for the Hotel class.
    """
    def setUp(self):
        # Create a hotel instance for testing
        self.hotel = Hotel.create_hotel("Test Hotel", "Test Location", 4)

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.hotel.filename):
            os.remove(self.hotel.filename)

    def test_create_hotel(self):
        """
        Test creating a new hotel.
        """
        # Positive test case for creating a hotel
        new_hotel = Hotel.create_hotel("New Hotel", "New Location", 3)
        self.assertIsNotNone(new_hotel)
        if new_hotel:
            os.remove(new_hotel.filename)

        # Negative test case for creating a hotel that already exists
        existing_hotel = Hotel.create_hotel("Test Hotel", "Test Location", 4)
        self.assertIsNone(existing_hotel)

    def test_modify_info(self):
        """
        Test for modying information.
        """
        # Modify hotel information
        self.hotel.modify_info(new_name="Modified Hotel",
        new_location="Modified Location",
        new_rating=5)
        self.assertEqual(self.hotel.name, "Modified Hotel")
        self.assertEqual(self.hotel.location, "Modified Location")
        self.assertEqual(self.hotel.rating, 5)

    def test_make_reservations(self):
        """
        Test to making reservations.
        """
        # Make reservations
        self.hotel.make_reservation()
        self.assertEqual(len(self.hotel.reservations), 1)

        # Make another reservation
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.hotel.make_reservation()
        self.assertEqual(len(self.hotel.reservations), 10)

    def test_cancel_reservation(self):
        """
        Test for canceling reservations.
        """
        # Cancel a reservation
        self.hotel.make_reservation()
        reservation_to_cancel = self.hotel.reservations[0]

        self.hotel.cancel_reservation(reservation_to_cancel)
        self.assertEqual(len(self.hotel.reservations), 0)
    def test_delete_hotel(self):
        """
        Test deleting a hotel.
        """
        # Verify hotel creation was successful
        self.assertIsNotNone(self.hotel)

        # Call delete_hotel method
        Hotel.delete_hotel(self.hotel)

        # Check if hotel file was deleted
        self.assertFalse(os.path.exists(self.hotel.filename))

if __name__ == '__main__':
    unittest.main()
# In[3]:
