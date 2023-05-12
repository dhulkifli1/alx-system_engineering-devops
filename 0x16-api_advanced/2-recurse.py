#!/usr/bin/python3
"""A module containing functions for working with the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and
    returns a list containing the titles of all hot articles for a subreddit
    """
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
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
