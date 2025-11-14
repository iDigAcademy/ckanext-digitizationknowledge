"""Tests for helpers.py."""

import ckanext.digitizationknowledge.helpers as helpers


def test_get_custom_featured_groups():
    """Test the get_custom_featured_groups helper function."""
    result = helpers.get_custom_featured_groups(count=1)
    assert isinstance(result, list)


def test_get_custom_featured_organizations():
    """Test the get_custom_featured_organizations helper function."""
    result = helpers.get_custom_featured_organizations(count=1)
    assert isinstance(result, list)
