"""Tests for views.py."""

import pytest

import ckanext.digitizationknowledge.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "digitizationknowledge")
@pytest.mark.usefixtures("with_plugins")
def test_digitizationknowledge_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("digitizationknowledge.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, digitizationknowledge!"
