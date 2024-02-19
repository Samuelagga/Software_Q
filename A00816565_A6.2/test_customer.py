"""
test_customer.py - Script that makes a unity test for the customer functions
"""

# !/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the libraries needed
import unittest
import os
from customer import Customers


# In[2]:
class TestCustomers(unittest.TestCase):
    """Class that contains the functions for the unit tests."""
    def setUp(self):
        self.customer = Customers.create_customer("John", "Doe", "123456")
        self.existing_customer = None
        if self.customer is None:
            self.existing_customer = Customers("John", "Doe", "123456")

    def tearDown(self):
        if os.path.exists(self.customer.filename):
            os.remove(self.customer.filename)
        if (self.existing_customer and
                os.path.exists(self.existing_customer.filename)):
            os.remove(self.existing_customer.filename)

    def test_create_customer(self):
        """Unit test for creating information of the customer"""
        self.assertIsNotNone(self.customer)
        self.assertIsNone(self.existing_customer)
        # Negative test case for creating a customer that already exists
        existing_customer = Customers.create_customer("John", "Doe", "123456")
        self.assertIsNone(existing_customer)

    def test_delete_customer(self):
        """Unit test for deleting information of the customer"""
        Customers.delete_customer(self.customer)
        self.assertFalse(os.path.exists(self.customer.filename))

    def test_show_info(self):
        """Unit test for showing information of the customer"""
        expected_info = "Name: John, Last Name: Doe, id number: 123456"
        self.assertEqual(expected_info, self.customer.show_info())

    def test_modify_info(self):
        """Unit test for modifying information of the customer"""
        self.customer.modify_info(new_name="Jane",
                                  new_last_name="Doe",
                                  new_id="654321")
        expected_info = "Name: Jane, Last Name: Doe, id number: 654321"
        self.assertEqual(expected_info, self.customer.show_info())

    def _get_last_printed_message(self):
        """Helper method to get the last printed message."""
        return self._testMethodDoc


if __name__ == '__main__':
    unittest.main()
# In[3]:
