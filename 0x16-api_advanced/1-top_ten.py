#!/usr/bin/python3
"""1-top_ten.py - Query Reddit API & find Top10 subreddits hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-custom-user-agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            title = post['data']['title']
            print(title)
    else:
        print(None)
