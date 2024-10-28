import pkgutil
import importlib
from app.commands import CommandRegistry, Command
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand
from app.commands import CommandRegistry
from app.plugins.history import HistoryManager
from app.plugins.csv import CsvCommand

class App:
    
    def __init__(self):
        self.registry = CommandRegistry()
        self.history_manager = HistoryManager()
        self.registry.register_command('add', AddCommand())
        self.registry.register_command('subtract', SubtractCommand())
        self.registry.register_command('multiply', MultiplyCommand())
        self.registry.register_command('divide', DivideCommand())
        self.registry.register_command('exit', ExitCommand())

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue
    def execute(self, command, *args):
        if command != 'exit' and command in self.registry.commands:
            history_manager = self.history_manager
            return self.registry.commands[command].execute(*args,history_manager), history_manager.history
        elif command == 'exit':
            return self.registry.commands[command].execute(*args)
        else:
            raise ValueError(f"Command '{command}' not found.")
    def run(self):
        history = []
        app = App()
        while True:
            command = input("Enter command (add, subtract, multiply, divide) or 'exit': ").lower()
            if command != 'exit' and command in self.registry.commands:
                try:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    result,history = app.execute(command, a, b)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error: {e}")
            elif command == "exit":
                 app.execute(command,history)
