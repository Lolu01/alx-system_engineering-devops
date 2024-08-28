#!/usr/bin/python3
"""
    Uses reddit API to get 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'myUserAgent/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        print(None)
        return

    data = response.json().get("data").get("children")
        posts = data['data'].get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(top_10_posts)
