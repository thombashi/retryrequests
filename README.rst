.. contents:: **retryrequests**
   :backlinks: top
   :depth: 2


Summary
============================================
A Python library for HTTP requests using requests package with exponential back-off retry.


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


Installation
============================================
::

    pip install retryrequests


Dependencies
============================================
Python 2.7+ or 3.4+

- `requests <http://python-requests.org/>`__
