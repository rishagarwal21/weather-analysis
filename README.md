# weather-analysis
Data problem related to weather

Overview
This program gives you insights from weather data for a particular month.

Assumptions:
Following assumptions have been made while writing this program.
--> Wind gust = 0, if value NA/NaN in data
--> Visibility = 0, if value NA/NaN in data
--> Pressure = 0, if value NA/NaN in data
--> Wind Speed values between 1 and 100 are valid
--> ScreenTemperature is in celsius and values between -15 and 50 are valid
#
Steps to run:
--> Run this command in your python venv "pip install -r /path/to/requirements.txt"
--> Update the module path in src/constants.py file.
--> Run report_test.py to check availability of data files
--> Run process.py to get report for specific date and results of problem
--> process.py takes one argument as date. Example: process.py --date 2016-03-01
#
Output:
--> Parquet files will be stored in /weather-analysis/part_files/
--> Reports generated through grouping of data will be stored in /weather-analysis/reports/
