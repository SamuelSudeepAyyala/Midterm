import logging
import logging.config
import sys
from app.commands import Command
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
class AddCommand(Command):

    def execute(self,x , y, history_manager):
        logging.info(f"Executing the Addition command with {x} and {y}")
        result = x + y
        logging.info(f"Calculated result: {result}")
        history_manager.add_to_history("Addition", x, y, result)
        logging.info("Addition History added")
        return result
