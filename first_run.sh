#!/bin/bash

# Prompt the user for start and end dates
read -p "Enter start date (YYYY-MM-DD): " START_DATE
read -p "Enter end date (YYYY-MM-DD): " END_DATE

# Run the Python script with the specified date range
START_DATE=$START_DATE END_DATE=$END_DATE python3 airelibre_data_extractor.py
