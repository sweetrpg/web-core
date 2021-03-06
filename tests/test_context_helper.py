# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_web_core.helpers.context import get_context
from flask import Flask, current_app


app = Flask(__name__)


def test_get_context():
    with app.test_request_context():
        context = get_context()
        assert isinstance(context, dict)
