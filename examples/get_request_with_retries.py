#!/usr/bin/env python3

import json

import retryrequests


r = retryrequests.get("https://kctbh9vrtdwd.statuspage.io/api/v2/status.json")
r.raise_for_status()

print(json.dumps(r.json(), indent=4))
