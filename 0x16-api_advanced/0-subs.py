#!/usr/bin/python3
"""
Contains number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and
    returns the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'my-custom-user-agent',
        'From': 'dhulkifliabbas06@gmail.com'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
