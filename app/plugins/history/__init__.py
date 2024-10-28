import logging
import os
import pandas as pd

class HistoryManager:
    def __init__(self, filename='calculation_history.csv'):
        self.history = []
        self.filename = filename

    def add_to_history(self, operation, operand1, operand2, result):
        entry = {
            "Operation": operation,
            "Operand1": operand1,
            "Operand2": operand2,
            "Result": result
        }
        logging.info(f"Appending the history with {entry}")
        self.history.append(entry)

    def get_history(self):
        return self.history

    def clear_history(self):
        logging.info("Clearing history")
        self.history.clear()
