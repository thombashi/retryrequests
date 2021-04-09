.. contents:: **retryrequests**
   :backlinks: top
   :depth: 2


Summary
============================================
A Python library that make HTTP requests with exponential back-off retry by using `requests <https://docs.python-requests.org/en/master/>`__ package.

.. image:: https://badge.fury.io/py/retryrequests.svg
    :target: https://badge.fury.io/py/retryrequests
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/retryrequests.svg
    :target: https://pypi.org/project/retryrequests
    :alt: Supported Python versions


Installation
============================================

::

    pip install retryrequests


Usage
============================================

:Sample Code:
    .. code-block:: python

        import json

        import retryrequests


        r = retryrequests.get("https://kctbh9vrtdwd.statuspage.io/api/v2/status.json")
        r.raise_for_status()

        print(json.dumps(r.json(), indent=4))

:Output:
    .. code-block:: json

        {
            "page": {
                "id": "kctbh9vrtdwd",
                "name": "GitHub",
                "url": "https://www.githubstatus.com",
                "time_zone": "Etc/UTC",
                "updated_at": "2019-03-30T07:11:24.851Z"
            },
            "status": {
                "indicator": "none",
                "description": "All Systems Operational"
            }
        }


Dependencies
============================================
Python 3.5+

- `requests <http://python-requests.org/>`__
