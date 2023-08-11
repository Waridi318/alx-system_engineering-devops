#!/usr/bin/python3
"""
This module contains a function that queries the
REDDIT API and returns the number of total subscribers
for a given subreddit
"""


from requests import get


def number_of_subscribers(subreddit):
    """queries the REDDIT API and returns the
    number of total subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }

    response = get(url, headers=headers)
    if response.status_code != 200:
        return(0)
    data = response.json()
    new_data = data['data']
    return(new_data['subscribers'])
