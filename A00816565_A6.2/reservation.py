"""
reservation.py - Script that generates functions used for making and
canceling reservations.
"""

# !/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the libraries needed
import json
import os


# In[2]:

class Reservation:
    """
    Class Reservation which contains the functions to make and
    delete a reservation.
    """
    def __init__(self, filename):
        self.filename = filename
        self.reservations = []

    def save_file(self):
        """
        Function to save the reservation data to a file.
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.reservations, f)

    def load_file(self):
        """
        Function to load the reservation data from a file.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.reservations = json.load(f)

    def create_reservation(self, customer_name, hotel_name, room_number):
        """
        Function to create a new reservation.
        """
        for reservation in self.reservations:
            if (reservation['hotel_name'] == hotel_name and
                    reservation['room_number'] == room_number):
                print(f"The room '{room_number}' in "
                      f"'{hotel_name}' is already reserved.")
                return
        reservation = {
            'customer_name': customer_name,
            'hotel_name': hotel_name,
            'room_number': room_number
        }
        self.reservations.append(reservation)
        self.save_file()

    def cancel_reservation(self, customer_name, hotel_name):
        """
        Function to cancel a reservation.
        """
        for reservation in self.reservations:
            if (reservation['customer_name'] == customer_name and
                    reservation['hotel_name'] == hotel_name):
                self.reservations.remove(reservation)
                self.save_file()
                print("Reservation canceled successfully.")
                return
        print("Reservation not found.")

# In[3]:
