from app.commands import Command
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
class SubtractCommand(Command):

    def execute(self,x , y, history_manager):
        result = x - y
        history_manager.add_to_history("Subtraction", x, y, result)
        return result

