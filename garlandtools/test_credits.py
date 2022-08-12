"""
Tests for Credits being correctly set in __init__.py
"""

from garlandtools import __credits__


def test_version():
    """
    Tests for Credits being correctly set in __init__.py
    """
    assert __credits__ == "GarlandTools"
