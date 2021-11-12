# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""Context helper functions.
"""

from flask import current_app, session, request
import os
from sweetrpg_web_core import constants
import hashlib


def get_context() -> dict:
    """Initialize a context object.

    :return:
    """
    email = session.get(constants.SESSION_EMAIL)
    email_hash = None
    gravatar_url = None
    if email:
        email_hash = hashlib.md5(email.strip().lower()).hexdigest()
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}"
    return {
        'user': {
            'id': session.get(constants.SESSION_USER_ID),
            'email': email,
            'email_hash': email_hash,
            'gravatar_url': gravatar_url,
        },
        'base_path': os.environ.get(constants.APPLICATION_BASE_PATH, ""),
        'static_asset_prefix': os.environ.get(constants.STATIC_ASSET_PREFIX, "")
    }


def populate_session() -> None:
    """Populate the session object with information from the incoming request.

    :return:
    """
    # Host: dev.sweetrpg.com
    # X-Real-Ip: 10.32.0.7
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
    # Accept-Encoding: gzip, deflate, br
    # Cookie: session=63e6f102-0b63-4576-9d1a-c9fdba16ba13; sweetrpg-auth=SrSVWUQeCGl_2cFbOQkyNS40zXOF1u4OJp0KJE3y-5sjr6mUviiCJda2Evrd375UMxg_ohwft_QgRyMlG8f3kY66WhVyKaIaAkBoYD1ruxexScFDL8whGg1-aOVs4v0PRoEPMcrMylacJ0-hhT_TgXGvHqFSyf5HuQb61R046oL2WztqEDnv4LFnXGWmDwzsmAtklz6jxZCuK8P0vWuWpLMdUkBHdwth-R2L1pSxscrH0SLLDA_mQPVpb6cHOTchNdxGMtp7CB79T87i8uB3jV1nHywexzg-ghj9_eHsRa_jH_hoc5wWsmzAzPW8cNWB_bfVh4I7sbMtYhSek5bSU4aZ3QuZJGHRKr3GJquEOzfrLf2MFrJj5VhH0bIXHKB6YqR9HRiJwJyySokiKropncqxVuuAQofd0vvNXd6lnL2R7E1Oq5_YkEzmZqvzMbylgn2TMZ6cRmnLagqnZade8LDG0TTFcGo3khP4SuDpgkx2q27uz7CiD6c-WxadwE8uxVnQ6tfSa7vrX9zXUtm44N9gZLGndQg4W0tj3nO2C8UwvjiMmAyUbQXA7GKDmPu3RZhoQ22y1IbKc0zN0zQP3YKNCSaIoeQoT1182Gtzj4EunIt-9eRAmGxKK0MBOHCH2Wq0rqLq5Sq9NdDILE8NkAq6SQHTl4CE_HeGpueq6QRmvZ6kFQJT9OxOrwRL0z6Y89SljFQ-5HeAyYvP3wqmlSW1aJ4nSBDP14xv-I_YpTW7KXaBFf2qSoxplGxSNyUVGD_PHl95vxYb4MycsILbkis6ivwMnwh4q1r32dZkg8tmhsocHUPwo1OS7OzD-K6DPmOXIOwfIZAAh2Mg179GG6u3DKYdsmQ2Tpv4tXnKm9AaryoT34T1vYDt2b4sLD8xXh0w8AMLwO88Q4sp2N6b0W4XAkHWadtUqIdDPdMHJQuam5fM1EFtQw6KPmeG1yasdGKaHk8drHrCltIcPpkXGC1Cwjs_gzDBxm2p68CkFZ7hlMXXbezIsLrNjwosGqNqgPrrk18KNjP2kmR1pfomQxTJF4AifAAAB6s4VsrKZT02FDlmJJP6AiKTtJNovVcrgoWld1WjrmZp3y4Jj1cWOhV7ZcAe7T7sjPlweBC1eIn9vlO5vDDDbIkaNqYvTtv3NOuwLQN2azmAt1_Vu6cpzYitZrlps80NzPNilWU-zI7caeIAFQBqX40bwBZXrUX88dIgJxNHCPePOBU6uM5Taddqk9cpKBzcG7T0pwF4XDTwhoTOkACqAtC26kwSwxuB2jSG6ZdXotsnTi-GnFaKZX6c6g0f_A44v_0AWch0PNV2v0AdSri9nMMBRkQ2HtkmoptV3LzvBpRkzZ0Boxfh0MafR4ugAWquNdxLlBJWATuTogmpiYdLPRw=|1635722526|tm8Zo044MaWFCyyO97ZD5VXPZJLfM9y1cKiC4NMYQ6Y=; ajs_anonymous_id=%2205a30181-160f-4a76-b562-7610a47369ea%22
    # Dnt: 1
    # Sec-Fetch-Mode: navigate
    # Sec-Fetch-User: ?1
    # Upgrade-Insecure-Requests: 1
    # X-Forwarded-Access-Token: C99_j-whvVVd3AgQ--S1RCQC7tpTNgd7
    # X-Forwarded-Email: paul@schifferers.net
    # X-Forwarded-For: 10.46.0.0, 10.32.0.3
    # X-Forwarded-Host: dev.sweetrpg.com
    # X-Forwarded-Port: 80
    # X-Forwarded-Proto: http
    # X-Forwarded-Server: traefik-m5tc5
    # X-Forwarded-User: github|419457
    current_app.logger.debug(f"SESSION: {session}")
    current_app.logger.debug(f"HEADERS: {request.headers}")
    current_app.logger.debug(f"COOKIES: {request.cookies}")
    current_app.logger.debug(f"ARGS: {request.args}")

    if constants.SWEETRPG_AUTH_KEY in request.cookies:
        current_app.logger.info("Setting user info from 'sweetrpg-auth' cookie.")
        userinfo = request.cookies[constants.SWEETRPG_AUTH_KEY]
        session[constants.PROFILE_KEY] = userinfo

    current_app.logger.info("Setting session values from request X-Forwarded-* headers")
    session[constants.SESSION_ACCESS_TOKEN] = request.headers.get("X-Forwarded-Access-Token")
    session[constants.SESSION_EMAIL] = request.headers.get("X-Forwarded-Email")
    session[constants.SESSION_USER_ID] = request.headers.get("X-Forwarded-User")
