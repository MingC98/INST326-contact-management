# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:19:56 2022

@author: 95192
"""

import re
import sys
import argparse

#User interface to ask the user for input
# They should be able to seach contact by name
    # If there is no match, it will allow them to add contact
    # Else they can choose either modify contact or delete contact
# May allow them to upload a csv/txt file

# Create a People class, will include name,phonenumber,address
# Create a Contact class contains a list of People object

# If the user put in the information
    #we just create the People object accordingly then append them into the Contact
# If they choose to upload a file
    # Open a file to read
    # Split the file into groups
    # Use the regular expression to get appropriate values
    # Append the value into the object then append it into the 