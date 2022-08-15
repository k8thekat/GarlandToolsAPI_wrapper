"""
Tests for Credits being correctly set in __init__.py
"""

from garlandtools import __version__, __author__, __credits__


def test_version():
    """
    Tests for Version being correctly set in __init__.py
    """
    assert __version__ == "0.1.0"


def test_author():
    """
    Tests for Author being correctly set in __init__.py
    """
    assert __author__ == "Lukas Weber"


def test_credits():
    """
    Tests for Credits being correctly set in __init__.py
    """
    assert __credits__ == "GarlandTools"
