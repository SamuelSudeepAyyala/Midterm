from abc import ABC,abstractmethod
class Command:
    @abstractmethod
    def execute(self,*args):
        pass

class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """Register a command with a given name."""
        if name in self.commands:
            raise ValueError(f"Command '{name}' is already registered.")
        self.commands[name] = command

    def execute_command(self, name, *args):
        """Execute a registered command by its name."""
        if name not in self.commands:
            raise ValueError(f"Command '{name}' not found.")
        return self.commands[name].execute(*args)