import requests
import pandas as pd
import datetime
import os

# Path to the CSV file
csv_file_path = 'data/airelibre_data.csv'

def fetch_data_for_day(date):
    """
    Fetch data for a specific day from the API and append it to the CSV file if it's not already present.
    """
    start_str = date.strftime('%Y-%m-%dT00:00')
    end_str = (date + datetime.timedelta(days=1)).strftime('%Y-%m-%dT00:00')

    # Check if the date's data already exists in the CSV
    if os.path.exists(csv_file_path):
        existing_data = pd.read_csv(csv_file_path, usecols=['recorded'], parse_dates=['recorded'])
        if any(existing_data['recorded'].dt.date == date.date()):
            print(f"Data for {start_str} already exists. Skipping.")
            return

    url = f"https://rald-dev.greenbeep.com/api/v1/measurements?start={start_str}&end={end_str}"
    
    try:
        response = requests.get(url, timeout=60)  # timeout to avoid hanging
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            
            if not df.empty:
                df['recorded'] = pd.to_datetime(df['recorded'])  # Ensure timestamps are parsed
                file_exists = os.path.exists(csv_file_path)
                
                # Append data, avoiding duplicates
                df.to_csv(csv_file_path, mode='a', header=not file_exists, index=False)
                print(f"Data for {start_str} to {end_str} appended to CSV.")
            else:
                print(f"No data found for {start_str} to {end_str}.")
        else:
            print(f"Error: {response.status_code} for {start_str} to {end_str}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {start_str} to {end_str}: {e}")

def fetch_data_in_range(start_date, end_date):
    """
    Fetch data for a date range, ensuring no duplicate entries in the CSV file.
    """
    current_date = start_date
    while current_date < end_date:
        fetch_data_for_day(current_date)
        current_date += datetime.timedelta(days=1)

if __name__ == "__main__":
    # Check for environment variables for start and end dates
    start_date = os.environ.get("START_DATE")
    end_date = os.environ.get("END_DATE")

    if start_date and end_date:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        fetch_data_in_range(start_date, end_date)
    else:
        # Default to extracting data for yesterday only
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        fetch_data_for_day(yesterday)
