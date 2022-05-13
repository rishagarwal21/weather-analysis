# weather-analysis
Data problem related to weather

---

  ##Overview
This program gives you insights from weather data for a particular month.<br />

  ##Assumptions:
      Following assumptions have been made while writing this program.<br /><br />

        Wind gust = 0, if value NA/NaN in data<br />
        Visibility = 0, if value NA/NaN in data<br />
        Pressure = 0, if value NA/NaN in data<br />
        Wind Speed values between 1 and 100 are valid<br />
        ScreenTemperature is in celsius and values between -15 and 50 are valid<br />

  ##Steps to run:
      Run this command in your python venv "pip install -r /path/to/requirements.txt"<br />
      Update the module path in src/constants.py file.<br />
      Run report_test.py to check availability of data files<br />
      Run process.py to get report for specific date and results of problem<br />
      process.py takes one argument as date. Example: process.py --date 2016-03-01<br />

---
  ##Output:
      Parquet files will be stored in /weather-analysis/part_files/<br />
      Reports generated through grouping of data will be stored in /weather-analysis/reports/<br />
