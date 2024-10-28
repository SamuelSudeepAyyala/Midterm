import logging
import sys
from app.commands import Command
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
class DivideCommand(Command):

    def execute(self,x , y, history_manager):
        if y == 0:
            logging.error("Divide By Zero triggered")
            raise ValueError("Cannot divide by zero!")
        logging.info(f"Executing the Addition command with {x} and {y}")
        result = x / y
        logging.info(f"Result of Division {result}")
        history_manager.add_to_history("Division", x, y, result)
        logging.info("Division History Added")
        return result
