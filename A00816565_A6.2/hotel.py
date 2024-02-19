"""
hotel.py - Script that generates functions used for creating,
deleting, modifying hotel info, as well as make and cancel
reservations.
"""

# !/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the libraries needed
import json
import os

# In[2]:

class Hotel:
    def __init__(self, name, location, rating):
        """
        Function to initialize hotel data.
        """
        self.name = name
        self.location = location
        self.rating = rating
        self.rooms = ['Room' + str(i) for i in range(1, 11)]  # Fixed 10 rooms
        self.reservations = []
        self.filename = f"hotel_{name}.json"

    def save_file(self):
        """
        Function to save the hotel data to a file.
        """
        data = {
            'name': self.name,
            'location': self.location,
            'rating': self.rating,
            'rooms': self.rooms,
            'reservations': self.reservations
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def create_hotel(name, location, rating):
        """
        Function to create a new hotel and save its info into a file.
        """
        # Check if hotel file already exists
        filename = f"hotel_{name}.json"
        if os.path.exists(filename):
            print("Hotel already exists. Try modifying the file")
            return None
        hotel = Hotel(name, location, rating)
        hotel.save_file()
        return hotel

    @staticmethod
    def delete_hotel(hotel):
        """
        Deletes hotel file.
        """
        os.remove(hotel.filename)

    def show_info(self):
        """
        Shows the hotel information.
        """
        return f"Hotel: {self.name}, Location: {self.location}, Rating: {self.rating}"

    def modify_info(self, new_name=None, new_location=None, new_rating=None):
        """
        Modifies information and updates the file. Takes None as default
        on the new hotel information.
        """
        if new_name:
            self.name = new_name
        if new_location:
            self.location = new_location
        if new_rating:
            self.rating = new_rating
        self.save_file()

    def make_reservation(self):
        """
        Function to make a reservation.
        """
        if self.rooms:
            room_number = self.rooms.pop(0)  # Automatically assign the lowest available room
            self.reservations.append(room_number)
            print(f"Reservation made for {room_number}.")
            self.save_file()  # Update file after making reservation
        else:
            print("No more rooms available.")

    def cancel_reservation(self, reservation_code):
        """
        Function to cancel a reservation.
        """
        if reservation_code in self.reservations:
            self.rooms.append(reservation_code)
            self.reservations.remove(reservation_code)
            print(f"Reservation {reservation_code} canceled.")
            self.save_file()  # Update file after canceling a reservation
        else:
            print("Reservation not found.")
    
# In[3]:
