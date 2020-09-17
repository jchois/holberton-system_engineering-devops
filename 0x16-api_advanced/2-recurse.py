#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    returns all hot articles for a given subreddit
    """

    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {'User-Agent': 'jchois'}
    arg1 = {"limit": 100, "after": after}
    resp = requests.get(url, params=arg1, headers=headers)
    new_list = resp.json().get('data', {}).get('children', None)
    pagination = resp.json().get('data', {}).get('after', None)

    if pagination is not None:
        if new_list:
            for item in new_list:
                hot_list.append(item.get("data").get("title"))

        if pagination is not None:
            recurse(subreddit, hot_list, pagination)

        return hot_list
    else:
        return None
