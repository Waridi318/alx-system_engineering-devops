#!/usr/bin/python3
"""
This module defines a function that queries the Reddit API
and returns a lit containing the titles of all hot articles
for a given subreddit
"""


from requests import get


def recurse(subreddit, hot_list=[], page=None):
    """
    queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16-api_advanced:v1.0.0"
    }
    if page:
        url += f"&after={page}"
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return (None)
    data = response.json()
    results = data.get("data").get("children")
    for post in results:
        title = post["data"]["title"]
        hot_list.append(title)
        print(title)

    page = data.get("data").get("after")
    if page is not None:
        return(recurse, hot_list, page)
    else:
        return(None)

    return(hot_list)
