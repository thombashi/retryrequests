"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from typing import Any, Dict, Optional, Sequence

import requests
from requests import Response, Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .__version__ import __author__, __copyright__, __email__, __license__, __version__


def make_requests_session(
    retries: int = 5, backoff_factor: float = 0.5, status_forcelist: Sequence[int] = (500, 502, 504)
) -> Session:
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


def get(url: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> Response:
    return make_requests_session().get(url, params=params, **kwargs)


def head(url: str, **kwargs) -> Response:
    return make_requests_session().head(url, **kwargs)


def post(url: str, data=None, json: Optional[Dict[str, Any]] = None, **kwargs) -> Response:
    return make_requests_session().post(url, data=data, json=json, **kwargs)


def put(url: str, data=None, **kwargs) -> Response:
    return make_requests_session().put(url, data=data, **kwargs)


def patch(url: str, data=None, **kwargs) -> Response:
    return make_requests_session().patch(url, data=data, **kwargs)


def delete(url: str, **kwargs) -> Response:
    return make_requests_session().delete(url, **kwargs)
