import logging
from app.commands import Command
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
class MultiplyCommand(Command):

    def execute(self,x , y, history_manager):
        logging.info(f"Execution of Multiplication for {x} and {y}")
        result = x * y
        logging.info(f"Multiplication result : {result}")
        history_manager.add_to_history("Multiplication", x, y, result)
        logging.info("Multiplication History Added")
        return result

