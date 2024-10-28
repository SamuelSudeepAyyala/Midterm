"""
Module for Testing Arithmetic Command Classes

This module contains unit tests for the arithmetic command classes 
implemented in the app.commands module. It includes tests for 
addition, subtraction, multiplication, and division commands, 
ensuring that each command behaves as expected under normal 
conditions and handles exceptional cases (like division by zero).
"""
import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand
from app.plugins.history import HistoryManager

history_manager = HistoryManager()
def test_add_command():
    """Test the functionality of the AddCommand."""
    command = AddCommand()
    result = command.execute(10, 5, history_manager)
    assert result == 15, f"Expected 15, got {result}"
    history = history_manager.get_history()
    assert len(history) == 1, "Expected history to have 1 entry"

def test_subtract_command():
    """Test the functionality of the SubtractCommand."""
    command = SubtractCommand()
    result = command.execute(10, 5, history_manager)
    assert result == 5, f"Expected 5, got {result}"
    history = history_manager.get_history()
    assert len(history) == 2, "Expected history to have 2 entries"

def test_multiply_command():
    """Test the functionality of the MultiplyCommand."""
    command = MultiplyCommand()
    result = command.execute(10, 5,history_manager)
    assert result == 50, f"Expected 50, got {result}"
    history = history_manager.get_history()
    assert len(history) == 3, "Expected history to have 3 entries"

def test_divide_command():
    """Test the functionality of the DivideCommand."""
    command = DivideCommand()
    result = command.execute(10, 5, history_manager)
    assert result == 2, f"Expected 2, got {result}"
    history = history_manager.get_history()
    assert len(history) == 4, "Expected history to have 4 entries"

def test_divide_by_zero():
    """Test the functionality of the DivideByZero in DivideCommand"""
    with pytest.raises(ValueError):
        command = DivideCommand()
        command.execute(10, 0, history_manager)

def test_exit_command_save_history(mocker):
    '''Testing the exit command and saving history'''
    history = [{'Operation': 'Addition', 'Operand1': 3, 'Operand2': 4, 'Result': 7}]
    mocker.patch('builtins.input', return_value='Y')
    mock_csv_command_execute = mocker.patch('app.plugins.csv.CsvCommand.execute')
    exit_command = ExitCommand()
    with pytest.raises(SystemExit):
        exit_command.execute(history)
    mock_csv_command_execute.assert_called_once()

def test_exit_command_no_save_history(mocker):
    '''Testing the exit command and not saving history'''
    history = [{'Operation': 'Addition', 'Operand1': 3, 'Operand2': 4, 'Result': 7}]
    mocker.patch('builtins.input', return_value='N')
    mock_csv_command_execute = mocker.patch('app.plugins.csv.CsvCommand.execute')
    exit_command = ExitCommand()
    with pytest.raises(SystemExit):
        exit_command.execute(history)
    mock_csv_command_execute.assert_not_called()
