#!/usr/bin/python3
"""
This module defines a function that queries
the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """queries
    the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print('None')
        return
    results = response.json()
#    print(results)
    new_data = results["data"]["children"]
    for data in new_data:
        title = data['data']['title']
        print(title)
