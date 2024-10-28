from app.commands import Command
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
class DivideCommand(Command):

    def execute(self,x , y, history_manager):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        result = x / y
        history_manager.add_to_history("Division", x, y, result)
        return result

