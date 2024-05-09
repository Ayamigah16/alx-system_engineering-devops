#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Custom",
        "Accept": "application/json",
    }
    response = requests.get(
        url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()["data"]
        return data["subscribers"]
    else:
        return 0
