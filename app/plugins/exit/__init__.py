import logging
import sys
from app.commands import Command
from app.plugins.csv import CsvCommand
from app.plugins.history import HistoryManager

class ExitCommand:

    def execute(self,history):
        # Export history to CSV
        if len(history) > 0:
            option = input("Do you want to save the history? Y or N :\n")
            if option == "Y":
                logging.info("Exiting after saving history")
                csv_run = CsvCommand(history)
                csv_run.execute()
                logging.info("History while saving: %s", str(history))
                print("Exiting the calculator.")
            elif option == "N":
                logging.info("Exiting without History")
                print("Exiting the calculator.")

        # Stop the application by raising SystemExit
        logging.info("Raising System Exit")
        raise SystemExit