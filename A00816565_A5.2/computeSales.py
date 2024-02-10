"""
computeSales.py - Script that verifies that receives the
products sold with its quantities, verifies the prices
and adds the values foe a total sum.

This script reads two .json files. Ones contains the library
of products and prices, while the other has the sales, and
quantities of the products bought. If the file is not compatible
it will display it in the console.

At the end it will print the results of the sum in the console
and creates and a file named "SalesResults.txt" with all the
gathered information.
"""

# !/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing the libraries needed
import json
import sys
import time

# In[2]:


def open_file(path):
    """
    Opens and reads data from a json file. It also anlyze if the
    file is not found or if it comes in an invalid json format.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid format")
        return None


# In[3]:

def sum_cost(product_list, sales_list):
    """
    Analyzing each sale in "sales file", it looks for the price
    of the product on the "product list". It then multiplies that
    price by the quantity of the sale. It finally adds all of the
    values of each sale into a total cost of the file.
    """
    total = 0
    for sale in sales_list:
        name = sale["Product"]
        quantity = sale["Quantity"]
        for product in product_list:
            if product["title"] == name:
                total += product["price"] * quantity
                break
    return total


# In[4]:

def main():
    """
    Main function to execute when the script is run. It adds up
    the total cost of the sales in "sales file". Then it prints
    the results in the console and writes them in a file called
    "SalesResults.txt.txt".
    """
    start_time = time.time()
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py"
              "priceCatalogue.json salesRecord.json")
        sys.exit(1)
    catalog_path = sys.argv[1]
    records_path = sys.argv[2]
    # Read json files
    price_catalog = open_file(catalog_path)
    sales_records = open_file(records_path)
    if price_catalog is None or sales_records is None:
        return
    # Calculate total cost
    total_cost = sum_cost(price_catalog, sales_records)
    time_elapsed = time.time() - start_time
    # Print results
    print("Total Cost:", total_cost)
    print("Time Elapsed:", time_elapsed, "seconds")
    # Write results on file
    with open("SalesResults.txt", 'w', encoding='utf-8') as result_file:
        result_file.write(f"Total Cost: {total_cost}\n")
        result_file.write(f"Time Elapsed: {time_elapsed} seconds\n")


if __name__ == "__main__":
    main()

# In[5]:
