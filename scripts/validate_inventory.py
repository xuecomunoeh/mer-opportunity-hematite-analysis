#!/usr/bin/env python3
"""
Validation script for image_inventory.csv.
Checks file existence, headers, column content.
"""

import csv
import os
import sys

def validate_csv(filepath):
    """Validate the CSV file according to specifications."""
    # Check file exists
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return False
    
    # Read CSV
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Check headers
            expected_headers = ['Sol', 'Instrument', 'Notes']
            if reader.fieldnames != expected_headers:
                print(f"Error: CSV headers are {reader.fieldnames}, expected {expected_headers}.")
                return False
            
            # Validate each row
            for i, row in enumerate(reader, start=2):  # row numbers start at 2 (header is row 1)
                # Validate Sol: positive integer
                sol = row.get('Sol', '').strip()
                if not sol.isdigit():
                    print(f"Error: Row {i}: Sol '{sol}' is not a positive integer.")
                    return False
                if int(sol) <= 0:
                    print(f"Error: Row {i}: Sol '{sol}' is not positive.")
                    return False
                
                # Validate Instrument: either 'Pancam' or 'Microscopic Imager'
                instrument = row.get('Instrument', '').strip()
                if instrument not in ('Pancam', 'Microscopic Imager'):
                    print(f"Error: Row {i}: Instrument '{instrument}' is not 'Pancam' or 'Microscopic Imager'.")
                    return False
                
                # Notes can be anything, no validation needed
            
            # All checks passed
            print("Validation successful")
            return True
            
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return False

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'image_inventory.csv')
    success = validate_csv(csv_path)
    sys.exit(0 if success else 1)