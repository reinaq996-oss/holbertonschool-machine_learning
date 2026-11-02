#!/usr/bin/env python3
"""Print the location of a GitHub user."""
import sys
import time

import requests


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json().get('location'))
    elif response.status_code == 404:
        print('Not found')
    elif response.status_code == 403:
        reset = int(response.headers.get('X-Ratelimit-Reset', 0))
        minutes = int((reset - time.time()) / 60)
        print('Reset in {} min'.format(minutes))
