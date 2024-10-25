"""
Module for Testing Command and CommandRegistry Classes

This module contains unit tests for the Command and CommandRegistry classes 
implemented in the app.commands module. It includes mock command classes 
for testing the registration and execution functionalities of the CommandRegistry.
"""
import pytest
from app.commands import Command, CommandRegistry
class MockCommand(Command):
    """Class for mocking addition command"""
    def execute(self, *args):
        return sum(args)

class AnotherMockCommand(Command):
    """Class for mocking subtraction command"""
    def execute(self, *args):
        return args[0] - args[1] if len(args) >= 2 else 0

def test_register_command():
    """Test the registration of commands in the CommandRegistry."""
    registry = CommandRegistry()
    mock_command = MockCommand()
    registry.register_command('add', mock_command)
    assert 'add' in registry.commands
    assert registry.commands['add'] == mock_command
    with pytest.raises(ValueError, match="Command 'add' is already registered."):
        registry.register_command('add', AnotherMockCommand())
def test_execute_command():
    """
    Test the execution of registered commands in the CommandRegistry.
    """
    registry = CommandRegistry()
    add_command = MockCommand()
    subtract_command = AnotherMockCommand()
    registry.register_command('add', add_command)
    registry.register_command('subtract', subtract_command)
    result_add = registry.execute_command('add', 3, 4, 5)
    assert result_add == 12
    result_subtract = registry.execute_command('subtract', 10, 3)
    assert result_subtract == 7
    with pytest.raises(ValueError, match="Command 'multiply' not found."):
        registry.execute_command('multiply', 3, 4)
