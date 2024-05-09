#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list of hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            return hot_list
        else:
            for post in posts:
                hot_list.append(post["data"]["title"])
            after = data["data"]["after"]
            return recurse(subreddit, hot_list, after)
    else:
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
