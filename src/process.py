#!/usr/bin/env python
__author__ = 'rishabhagarwal'

import os
import sys
import argparse
import datetime
import pandas as pd
import constants

sys.path.append(constants.MODULE_PATH)


class WeatherReport:
    def __init__(self):
        pass

    @staticmethod
    def checkFileExist(file_name):
        if os.path.exists(file_name):
            print("File Found:", file_name)
            return True
        else:
            print("File Not Found:", file_name)
            exit(0)

    @staticmethod
    def checkFolderExist(temp_folder):
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

    @staticmethod
    def clean_data(df):
        df['WindGust'] = df['WindGust'].fillna(0)
        df['Visibility'] = df['Visibility'].fillna(0)
        df['Pressure'] = df['Pressure'].fillna(0)
        df1 = df[df['WindSpeed'].between(1, 100)]
        df_temp_corrected = df1[df1['ScreenTemperature'].between(-15, 50)]
        return df_temp_corrected

    @staticmethod
    def get_insights(grouped_df):
        max_temp = grouped_df['ScreenTemperature'].max()
        df2 = grouped_df.loc[grouped_df['ScreenTemperature'] == max_temp, 'ObservationDate'].iloc[0]
        df3 = grouped_df.loc[grouped_df['ScreenTemperature'] == max_temp, 'Region'].iloc[0]
        print("Which date was the hottest day? : ", df2)
        print("What was the temperature on that day? : ", max_temp)
        print("In which region was the hottest day? : ", df3)

    def ConvertToParquet(self, file_name):
        file_path = constants.DATA_DIR + file_name
        pd.set_option('display.max_columns', None)
        df = pd.read_csv(file_path)
        df["ObservationDate"] = pd.to_datetime(df["ObservationDate"])
        df["ObservationDate"] = df["ObservationDate"].astype(str)
        partition_val = 'ObservationDate'
        self.checkFolderExist(constants.PARQ_DIR)
        df.to_parquet(constants.PARQ_DIR, partition_cols=[partition_val], index=False)
        return df

    def get_data(self, file_date):
        file_name = constants.FILE_PREFIX + file_date + constants.FILE_EXT
        self.checkFileExist(constants.DATA_DIR + file_name)
        raw_df = self.ConvertToParquet(file_name)
        return raw_df

    def create_report(self, report_date):
        raw_data = self.get_data(report_date)
        clean_df = self.clean_data(raw_data)
        grouped_df = clean_df.groupby(
            ['ForecastSiteCode', 'ObservationDate', 'SiteName', 'Latitude', 'Longitude', 'Region', 'Country'])[
            ["WindSpeed", "WindGust", "Visibility", "ScreenTemperature", "Pressure"]].mean().reset_index()
        self.checkFolderExist(constants.REPORT_DIR)
        grouped_df.to_csv(constants.REPORT_DIR + 'report.' + report_date + '.csv', index=False)
        self.get_insights(grouped_df)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", dest="exec_date", default=None, help="execution date")
    args = parser.parse_args()
    exec_date = (datetime.datetime.strptime(args.exec_date, '%Y-%m-%d').date()).strftime('%Y%m%d')
    weather_util = WeatherReport()
    weather_util.create_report(exec_date)
