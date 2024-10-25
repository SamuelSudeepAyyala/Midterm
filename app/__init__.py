from app.commands import CommandRegistry, Command
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self):
        self.registry = CommandRegistry()

        # Register available commands
        self.registry.register_command('add', AddCommand())
        self.registry.register_command('subtract', SubtractCommand())
        self.registry.register_command('multiply', MultiplyCommand())
        self.registry.register_command('divide', DivideCommand())

    def run(self):
        print("Welcome to the REPL Calculator")
        while True:
            user_input = input("Enter command (add, subtract, multiply, divide) or 'exit' to exit: ").strip().lower()

            if user_input == 'exit':
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

# Running the REPL
if __name__ == "__main__":
    repl = REPL()
    repl.run()
