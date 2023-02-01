#!/usr/bin/python3
"""
Queries the Reddit API and
returns a list containing the titles of all hot articles for a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and
    returns a list containing the titles of all hot articles for a subreddit
    """
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'dhulkifliabbas06@gmail.com'
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_posts = data.get('data').get('children')
    for post in hot_posts:
        hot_list.append(post.get('data').get('title'))

    after = data.get('data').get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
