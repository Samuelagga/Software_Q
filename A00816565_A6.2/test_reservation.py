"""
test_reservation.py - Script that makes a unity test
for the reservation functions
"""

# !/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the libraries needed
import unittest
import os
import sys
from io import StringIO
from reservation import Reservation


# In[2]:

class TestReservation(unittest.TestCase):
    """Class that contains the functions for the unit tests."""
    def setUp(self):
        self.reservation_file = "test_reservations.json"
        self.reservation = Reservation(self.reservation_file)

    def tearDown(self):
        if os.path.exists(self.reservation_file):
            os.remove(self.reservation_file)

    def test_create_reservation(self):
        """Unit test for creating a new reservation"""
        self.reservation.create_reservation("John Doe", "Hotel A", "101")
        self.assertTrue(os.path.exists(self.reservation_file))
        self.reservation.load_file()
        self.assertEqual(len(self.reservation.reservations), 1)

    def test_cancel_reservation(self):
        """Unit test for canceling a reservation"""
        self.reservation.create_reservation("John Doe", "Hotel A", "101")
        self.reservation.load_file()
        self.assertEqual(len(self.reservation.reservations), 1)

        self.reservation.cancel_reservation("John Doe", "Hotel A")
        self.reservation.load_file()
        self.assertEqual(len(self.reservation.reservations), 0)

    def test_existing_reservation(self):
        """Negative test for creating a new reservation"""
        self.reservation.create_reservation("John Doe", "Hotel A", "101")
        self.reservation.load_file()
        self.assertEqual(len(self.reservation.reservations), 1)

        # Try to create the same reservation again
        self.reservation.create_reservation("John Doe", "Hotel A", "101")
        self.reservation.load_file()
        # Ensure that no new reservation is added
        self.assertEqual(len(self.reservation.reservations), 1)
        # Check if the reservation already exists
        self.assertEqual("The room '101' in 'Hotel A' is already reserved.",
                         self._get_last_printed_message())

    def _get_last_printed_message(self):
        """Helper method to get the last printed message."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.reservation.create_reservation("John Doe", "Hotel A", "101")
        sys.stdout = sys.__stdout__  # Reset redirect
        return captured_output.getvalue().strip()


if __name__ == '__main__':
    unittest.main()
# In[3]:
