"""Tests for helpers.py."""

import ckanext.digitizationknowledge.helpers as helpers


def test_digitizationknowledge_hello():
    assert helpers.digitizationknowledge_hello() == "Hello, digitizationknowledge!"
