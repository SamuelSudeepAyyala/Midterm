import pkgutil
import importlib
import os
import logging
from dotenv import load_dotenv
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
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')

        self.registry = CommandRegistry()
        self.history_manager = HistoryManager()
        self.registry.register_command('add', AddCommand())
        self.registry.register_command('subtract', SubtractCommand())
        self.registry.register_command('multiply', MultiplyCommand())
        self.registry.register_command('divide', DivideCommand())
        self.registry.register_command('exit', ExitCommand())

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

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
                    logging.error(f"Error: {e}")
            elif command == "exit":
                 app.execute(command,history)
