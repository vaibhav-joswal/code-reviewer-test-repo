# Save this file as 'big_test_file.py'

import os, sys # E401: multiple imports on one line
import json    # F401: 'json' is imported but never used

# D100: Missing docstring in public module

def get_user_details(user_id):
    """
    Retrieves user details from a mock database.
    This function has a good docstring.
    """
    db = {
        1: "Alice Smith",
        2: "Bob Johnson"
    }
    return db.get(user_id, "Unknown User")


def process_data(data_list):
    # D103: Missing docstring in public function
    
    processed =[] # E225: missing whitespace around operator
    for item in data_list:
        if item > 10:
            processed.append(item * 2)
    
    print("Data processing complete") # E231: missing whitespace after ','
    return processed


class dataManager: # N801: class name should use CapWords (DataManager)
    # D101: Missing docstring in public class

    def __init__(self, raw_data):
        # D107: Missing docstring in __init__
        self.data = raw_data

    def get_data(self):
        # D102: Missing docstring in public method
        return self.data

# E305: expected 2 blank lines after class definition
print("Module loaded.")
