import pkgutil
import importlib
from app.commands import CommandRegistry, Command
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.commands import CommandRegistry
from app.commands import Command

class App:
    def __init__(self):
        self.registry = CommandRegistry()
        self.registry.register_command('add', AddCommand())
        self.registry.register_command('subtract', SubtractCommand())
        self.registry.register_command('multiply', MultiplyCommand())
        self.registry.register_command('divide', DivideCommand())

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
    def run(self):
        print("Welcome to the REPL Calculator")
        while True:
            user_input = input("Enter command (add, subtract, multiply, divide) or 'exit' to exit: ").strip().lower()

            if user_input == 'exit':
                print("Exiting....")
                break

            if user_input in self.registry.commands:
                try:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue

                try:
                    result = self.registry.execute_command(user_input, x, y)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print(f"Unknown command: {user_input}")


if __name__ == "__main__":
    app = App()
    app.start()