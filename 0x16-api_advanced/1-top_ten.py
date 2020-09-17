#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """top 10 posts"""
    URL = 'http://reddit.com/r/{}/hot.json'
    headers = {"User-Agent": "jchois"}

    response = requests.get(URL.format(subreddit), params={
                            'limit': 10}, headers=headers)

    posts = response.json().get('data', {}).get('children', None)

    if posts:
        for titles in posts:
            print(titles.get('data').get('title'))
    else:
        print('None')
