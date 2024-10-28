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
        if not isinstance(self.history_manager, list) or not all(isinstance(i, dict) for i in self.history_manager):
            logging.error("Invalid data format in history manager. Expected a list of dictionaries.")
            return
        
        # Create a DataFrame from the history list
        df = pd.DataFrame(history)
        file_exists = os.path.isfile(self.filename)

        # Export to CSV
        df.to_csv(self.filename, mode='a', header=not file_exists, index=False)
        logging.info(f"History exported to {self.filename} in the specified format.")
