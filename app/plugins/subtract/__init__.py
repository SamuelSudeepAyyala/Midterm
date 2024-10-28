import logging
from app.commands import Command
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
class SubtractCommand(Command):

    def execute(self,x , y, history_manager):
        logging.info(f"Executing Subtract operation on {x} and {y}")
        result = x - y
        logging.info(f"SUbtraction Result: {result}")
        history_manager.add_to_history("Subtraction", x, y, result)
        logging.info("Division result Added to History")
        return result

