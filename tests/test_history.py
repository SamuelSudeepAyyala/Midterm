"""
Test module for the HistoryManager class.

This module contains tests to ensure that the HistoryManager class behaves as expected 
when managing calculator operation history. It verifies the ability to add entries to the 
history, retrieve the current history, and clear all history entries.
"""
from app.plugins.history import HistoryManager
def test_add_to_history():
    """
    Test that a new operation is added to the history.

    This test checks if the HistoryManager correctly adds a new operation entry to the 
    history and verifies that the entry's details match the provided inputs.
    """
    history_manager = HistoryManager()
    operation = "Addition"
    operand1, operand2, result = 5, 3, 8
    history_manager.add_to_history(operation, operand1, operand2, result)

    history = history_manager.get_history()
    assert len(history) == 1, "Expected history to have 1 entry"
    assert history[0]["Operation"] == operation
    assert history[0]["Operand1"] == operand1
    assert history[0]["Operand2"] == operand2
    assert history[0]["Result"] == result


def test_get_history():
    """
    Test that the history can be retrieved correctly.

    This test checks if the HistoryManager returns the correct history as a list, 
    containing the expected details of previously added operations.
    """
    history_manager = HistoryManager()
    operation = "Subtraction"
    operand1, operand2, result = 10, 4, 6
    history_manager.add_to_history(operation, operand1, operand2, result)

    history = history_manager.get_history()

    assert isinstance(history, list), "Expected history to be a list"
    assert len(history) == 1, "Expected history to have 1 entry"
    assert history[0]["Operation"] == operation
    assert history[0]["Operand1"] == operand1
    assert history[0]["Operand2"] == operand2
    assert history[0]["Result"] == result


def test_clear_history():
    """
    Test that the history can be cleared.

    This test verifies that calling the clear_history method on the HistoryManager 
    removes all entries from the history, resulting in an empty history.
    """
    history_manager = HistoryManager()
    history_manager.add_to_history("Multiplication", 2, 3, 6)

    history_manager.clear_history()

    assert len(history_manager.get_history()) == 0, "Expected history to be empty after clearing"
