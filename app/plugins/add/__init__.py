from app.commands import Command
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
class AddCommand(Command):

    def execute(self,x , y, history_manager):
        result = x + y
        history_manager.add_to_history("Addition", x, y, result)
        return result

