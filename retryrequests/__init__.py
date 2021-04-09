"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import requests
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .__version__ import __author__, __copyright__, __email__, __license__, __version__


def make_requests_session(retries=5, backoff_factor=0.5, status_forcelist=(500, 502, 504)):
    session = Session()
    adapter = HTTPAdapter(
        max_retries=Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def get(url, params=None, **kwargs):
    return make_requests_session().get(url, params=params, **kwargs)


def head(url, **kwargs):
    return make_requests_session().head(url, **kwargs)


def post(url, data=None, json=None, **kwargs):
    return make_requests_session().post(url, data=data, json=json, **kwargs)


def put(url, data=None, **kwargs):
    return make_requests_session().put(url, data=data, **kwargs)


def patch(url, data=None, **kwargs):
    return make_requests_session().patch(url, data=data, **kwargs)


def delete(url, **kwargs):
    return make_requests_session().delete(url, **kwargs)
