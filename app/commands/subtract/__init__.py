from app.commands import Command
class SubtractCommand(Command):
    def execute(self, x, y):
        return x - y