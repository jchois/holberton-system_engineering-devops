#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """comments"""
    headers = {"User-Agent": "jchois"}
    response = requests.get('https://reddit.com/r/' +
                            subreddit + '/about.json', headers=headers)

    if response.status_code != 200:
        return 0

    return response.json().get('data', {}).get('subscribers', 0)
