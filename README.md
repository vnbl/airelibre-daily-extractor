# AireLibre Daily Extractor

This project automates the extraction of daily data from the AireLibre API and saves it into a CSV file. It supports both scheduled daily updates and an initial extraction for a specified date range.

---

## Features
- **Daily Updates**: Automatically fetches data for the previous day via a cron job.
- **First Run**: Allows the user to specify a date range for initial data extraction.
- **Deduplication**: Ensures no duplicate data is added to the CSV file.

---

## Prerequisites
1. Python 3.7 or higher installed on your system.
2. `pip` for installing Python packages.
3. Cron installed for scheduling daily jobs.

---

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:vnbl/airelibre-daily-extractor.git
   ```

2. Navigate to the repository:
    ```bash
    cd airelibre-daily-extractor
    ```
3. Create a virtual environment
    ```bash
    python3 -m venv venv
    ```
4. activate the virtual environment:
    - On Linux/Mac:
    ```bash
    source venv/bin/activate
    ```
    - On Windows:
    ```bash
    venv\Scripts\activate
    ```
5. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    Note: Create a requirements.txt file if not already present and list dependencies like pandas and requests.

6. Ensure the output directory exists:
    ```bash
    mkdir -p data
    ```

Usage
1. First-Time Data Extraction

For the initial extraction, use the first_run.sh script:
```bash
chmod +x first_run.sh # make sure it's executable
./first_run.sh
 ```

Follow the prompts to specify the start and end dates (in YYYY-MM-DD format) for the data extraction. For example:
```bash
Enter start date (YYYY-MM-DD): 2023-01-01
Enter end date (YYYY-MM-DD): 2023-12-31
```

This will extract data from January 1, 2023, to December 31, 2023, and save it to `data/airelibre_data.csv`.

2. Daily Data Updates

Set up the daily cron job to automatically fetch data for the previous day.
### Create a Daily Run Script

The run_daily.sh script handles daily updates:
```bash
chmod + run_daily.sh
./run_daily.sh
```
### Set Up the Cron Job

1. Open the crontab editor:
    ```bash
    crontab -e
    ```

2. Add the following line to schedule the script to run daily at 2 AM:
    ```bash
    0 2 * * * /path/to/repository/run_daily.sh >> /path/to/repository/log.txt 2>&1
    ```

3. Replace `/path/to/repository` with the full path to the cloned repository.

4. Save and exit the editor.

## Project Structure

```
airelibre-daily-extractor/
├── airelibre_data_extractor.py  # Python script for API extraction
├── first_run.sh                 # Shell script for initial data extraction
├── run_daily.sh                 # Shell script for daily updates
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
└── data/raw/                 # Directory for storing extracted CSV files
```
## CSV File Details

- File Path: `data/airelibre_data.csv`
- Columns: Dynamically determined by the API response.
- The script ensures no duplicate data is added.

## Environment Variables (Optional)

You can pass custom start and end dates to the Python script using environment variables:
```bash
START_DATE=2023-11-01 END_DATE=2023-11-30 python3 airelibre_data_extractor.py
```

## Logging

All output from the cron job is logged to `log.txt` in the repository directory. Review this file for debugging or monitoring.

## Contributing

Feel free to submit issues or pull requests to improve the project.
## License

This project is licensed under GNU Affero 3.0

## Author

Fernanda Carlés
GitHub: @vnbl