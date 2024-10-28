import logging
import os
from app.commands import Command
import pandas as pd


class CsvCommand(Command):
    def __init__(self, history_manager, filename='calculator_history.csv'):
        self.history_manager = history_manager
        self.filename = os.path.join('data', filename)

    def execute(self):

        # Ensure the 'data' directory exists and is writable
        data_dir = './data'
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            logging.info(f"The directory '{data_dir}' is created")

        elif not os.access(data_dir, os.W_OK):
            logging.error(f"The directory '{data_dir}' is not writable.")
            return
        
        history = self.history_manager
        
        # Create a DataFrame from the history list
        df = pd.DataFrame(history)
        file_exists = os.path.isfile(self.filename)

        # Export to CSV
        df.to_csv(self.filename, mode='a', header=not file_exists, index=False)
        print(f"History exported to {self.filename} in the specified format.")
        
    def display_csv(self):
        csv_file_path = os.path.join(self.data_dir, self.history_file)
        if os.path.exists(csv_file_path):
            df = pd.read_csv(csv_file_path)
            print("Calculation History:")
            logging.info("Displaying calculation history.")
            for index, row in df.iterrows():
                print(f"{row['Operation']}({row['Operand1']}, {row['Operand2']}) = {row['Result']}")
                logging.info(f"Record {index}: {row['Operation']}({row['Operand1']}, {row['Operand2']}) = {row['Result']}")
        else:
            logging.warning(f"No calculation history found at '{csv_file_path}'")
            print("No calculation history found.")

