#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a subreddit
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'my-custom-user-agent',
        'From': 'dhulkifliabbas06@gmail.com'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            title = post['data']['title']
            print(title)
    else:
        print(None)
