"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.digitizationknowledge.logic import validators


def test_digitizationknowledge_reauired_with_valid_value():
    assert validators.digitizationknowledge_required("value") == "value"


def test_digitizationknowledge_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.digitizationknowledge_required(None)
