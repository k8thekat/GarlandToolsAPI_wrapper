"""
Tests for Author being correctly set in __init__.py
"""

from garlandtools import __author__


def test_author():
    """
    Tests for Author being correctly set in __init__.py
    """
    assert __author__ == "Lukas Weber"
