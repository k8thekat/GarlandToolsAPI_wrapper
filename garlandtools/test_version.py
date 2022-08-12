"""
Tests for Version being correctly set in __init__.py
"""

from garlandtools import __version__


def test_version():
    """
    Tests for Version being correctly set in __init__.py
    """
    assert __version__ == "0.1.0"
