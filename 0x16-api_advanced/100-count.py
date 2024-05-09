#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of
    given keywords
    """
    if len(counts) == 0:
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(
        url, headers=headers,
        params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if not posts:
            sorted_counts = sorted(
                counts.items(), key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
            return
        else:
            for post in posts:
                title = post["data"]["title"].lower()
                for word in word_list:
                    if word.lower() in title:
                        counts[word.lower()] += title.count(
                            word.lower())
            after = data["data"]["after"]
            return count_words(
                subreddit, word_list, after, counts)
    else:
        return
