"""
Test module for the CsvCommand class.

This module contains tests to ensure that the CsvCommand class behaves as expected when handling 
CSV files for storing calculator operation history. It verifies that the class can append data 
to an existing file, create a new file if it does not exist, and handle invalid data gracefully.
"""
import os
import pandas as pd
import pytest
from app.plugins.csv import CsvCommand
DATA_DIR = './data'
CSV_FILENAME = 'calculator_history.csv'
CSV_PATH = os.path.join(DATA_DIR, CSV_FILENAME)


@pytest.fixture(scope="module", autouse=True)
def setup_csv_file():
    """
    Fixture to set up the CSV file before tests run.

    This function creates a directory for data if it does not exist, removes any existing CSV file 
    with the same name, and populates it with initial data for the tests.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    if os.path.isfile(CSV_PATH):
        os.remove(CSV_PATH)
    if not os.path.isfile(CSV_PATH):
        initial_data = [
            {'Operation': 'Addition', 'Operand1': 32.0, 'Operand2': 43.0, 'Result': 75.0},
            {'Operation': 'Subtraction', 'Operand1': 32.0, 'Operand2': 12.0, 'Result': 20.0}
        ]
        csv_command = CsvCommand(initial_data, filename=CSV_FILENAME)
        csv_command.execute()


def test_csv_command_appends_to_existing_file(setup_csv_file):
    """
    Test that CsvCommand appends data to an existing CSV file.

    This test verifies that a new entry is appended to the existing CSV file and that the 
    appended data is correct.
    """
    new_history = [{'Operation': 'Addition', 'Operand1': 5.0, 'Operand2': 3.0, 'Result': 8.0}]
    csv_command = CsvCommand(new_history, filename=CSV_FILENAME)  # Use CSV_PATH here
    csv_command.execute()
    df = pd.read_csv(CSV_PATH)
    print(df)
    assert df.shape[0] == 3, "Data was not appended to the existing CSV file."
    assert (df.iloc[-1] == pd.Series({'Operation': 'Addition', 'Operand1': 5.0, 'Operand2': 3.0, 'Result': 8.0})).all(), "New entry was not appended correctly."


def test_csv_command_creates_file_if_not_exist():
    """
    Test that CsvCommand creates a new CSV file if it does not exist.

    This test checks that a new CSV file is created with the correct data if it does not 
    already exist.
    """
    if os.path.isfile(CSV_PATH):
        os.remove(CSV_PATH)
    new_history = [{'Operation': 'Multiplication', 'Operand1': 5.0, 'Operand2': 3.0, 'Result': 15.0}]
    csv_command = CsvCommand(new_history, filename=CSV_FILENAME)  # Use CSV_PATH here
    csv_command.execute()
    df = pd.read_csv(CSV_PATH)
    assert df.shape[0] == 1, "New CSV file should contain 1 entry."
    assert (df.iloc[0] == pd.Series({'Operation': 'Multiplication', 'Operand1': 5.0, 'Operand2': 3.0, 'Result': 15.0})).all(), "New entry was not written correctly."


def test_csv_command_does_not_write_invalid_data():
    """
    Test that CsvCommand does not write invalid data to the CSV file.

    This test ensures that if invalid data is passed to the CsvCommand, the CSV file remains 
    unchanged.
    """
    invalid_history = "This is not a valid history"
    csv_command = CsvCommand(invalid_history, filename=CSV_FILENAME)
    csv_command.execute()
    df = pd.read_csv(CSV_PATH)
    assert df.shape[0] == 1, "CSV file should remain unchanged with invalid data."
