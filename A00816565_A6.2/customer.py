"""
customer.py - Script that generates functions used for creating,
deleting and modifying customers info.
"""

# !/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the libraries needed
import json
import os

# In[2]:

class Customers:
    def __init__(self, name, last_name, id):
        """
        Function to initialize customer data.
        """
        self.name = name
        self.last_name = last_name
        self.id = id
        self.filename = f"Customer_{id}.json"

    def save_file(self):
        """
        Function to save the customer data to a file.
        """
        data = {
            'name': self.name,
            'last_name': self.last_name,
            'id': self.id
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def create_customer(name, last_name, id):
        """
        Function to create a new customer and save its info into a file.
        """
        # Check if customer already exists
        filename = f"Customer_{id}.json"
        if os.path.exists(filename):
            print("Customer already exists.")
            return None
        customer = Customers(name, last_name, id)
        customer.save_file()
        return customer

    @staticmethod
    def delete_customer(customer):
        """
        Deletes customer file.
        """
        os.remove(customer.filename)

    def show_info(self):
        """
        Shows the customer information.
        """
        return f"Name: {self.name}, Last Name: {self.last_name}, id: {self.id}"

    def modify_info(self, new_name=None, new_last_name=None, new_id=None):
        """
        Modifies information and updates the file. Takes None as default
        on the new customer information.
        """
        if new_name:
            self.name = new_name
        if new_last_name:
            self.last_name = new_last_name
        if new_id:
            self.id = new_id
        self.save_file()
# In[3]:
