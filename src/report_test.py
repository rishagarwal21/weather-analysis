import os
import pytest
import process
import constants


def test_file1_available():
    assert process.WeatherReport.checkIfFileExist(constants.DATA_DIR + 'weather.20160301.csv') == True


def test_file2_available():
    assert process.WeatherReport.checkIfFileExist(constants.DATA_DIR + 'weather.20160201.csv') == True


