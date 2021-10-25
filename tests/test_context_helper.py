# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_web_core.helpers.context import get_context


def test_get_context():
    context = get_context()
    assert isinstance(context, dict)
