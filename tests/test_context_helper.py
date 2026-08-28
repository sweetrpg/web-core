# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import hashlib

from sweetrpg_web_core import constants
from sweetrpg_web_core.helpers.context import get_context
from flask import Flask, session


app = Flask(__name__)
app.config["SECRET_KEY"] = "test"


def test_get_context():
    with app.test_request_context():
        context = get_context()
        assert isinstance(context, dict)


def test_get_context_hashes_email_for_gravatar():
    with app.test_request_context():
        session[constants.SESSION_EMAIL] = "User@Example.com"
        context = get_context()
        expected_hash = hashlib.md5(b"user@example.com").hexdigest()
        assert context["user"]["email_hash"] == expected_hash
        assert (
            context["user"]["gravatar_url"]
            == f"https://www.gravatar.com/avatar/{expected_hash}?s=64&d=404"
        )


def test_get_context_derives_avatar_initial_and_admin_flag():
    with app.test_request_context():
        session[constants.SESSION_NAME] = "Paul Schifferer"
        session[constants.SESSION_ROLES] = ["admin"]
        context = get_context()
        assert context["user"]["name"] == "Paul Schifferer"
        assert context["user"]["avatar_initial"] == "P"
        assert context["user"]["is_admin"] is True


def test_get_context_non_admin_has_no_admin_flag():
    with app.test_request_context():
        session[constants.SESSION_NAME] = "Regular User"
        session[constants.SESSION_ROLES] = ["member"]
        context = get_context()
        assert context["user"]["avatar_initial"] == "R"
        assert context["user"]["is_admin"] is False
