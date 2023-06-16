#!/usr/bin/python3
""" A module that contains a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If
you’re getting errors related to Too Many Requests, ensure you’re setting a
custom User-Agent.

Requirements:
Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are not following redirects
"""
import requests


def number_of_subscribers(subreddit):
    """A function that reads from the reddit's API and returns the
    number subscribers
    """
    my_client = requests.session()

    # Set custom `User-Agent` header to avoid "too many requests error (429)"
    my_client.headers['User-Agent'] = 'Custom User Agent for task 0'

    url = 'https://www.reddit.com/r/{:s}/about.json'.format(subreddit)
    r = my_client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return 0
