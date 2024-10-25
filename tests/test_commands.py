"""
Module for Testing Arithmetic Command Classes

This module contains unit tests for the arithmetic command classes 
implemented in the app.commands module. It includes tests for 
addition, subtraction, multiplication, and division commands, 
ensuring that each command behaves as expected under normal 
conditions and handles exceptional cases (like division by zero).
"""
import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

def test_add_command():
    """Test the functionality of the AddCommand."""
    command = AddCommand()
    result = command.execute(10, 5)
    assert result == 15, f"Expected 15, got {result}"

def test_subtract_command():
    """Test the functionality of the SubtractCommand."""
    command = SubtractCommand()
    result = command.execute(10, 5)
    assert result == 5, f"Expected 5, got {result}"

def test_multiply_command():
    """Test the functionality of the MultiplyCommand."""
    command = MultiplyCommand()
    result = command.execute(10, 5)
    assert result == 50, f"Expected 50, got {result}"

def test_divide_command():
    """Test the functionality of the DivideCommand."""
    command = DivideCommand()
    result = command.execute(10, 5)
    assert result == 2, f"Expected 2, got {result}"

def test_divide_by_zero():
    """Test the functionality of the DivideByZero in DivideCommand"""
    with pytest.raises(ValueError):
        command = DivideCommand()
        command.execute(10, 0)
