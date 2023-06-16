#!/usr/bin/python3
"""A module that contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the function
should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:
- Prototype: def recurse(subreddit, hot_list=[])
- Note: You may change the prototype, but it must be able to be called with
  just a subreddit supplied. AKA you can add a counter, but it must work
  without supplying a starting value in the main.
- If not a valid subreddit, return None.

NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are not following redirects.
Your code will NOT pass if you are using a loop and not recursively calling
the function! This "can" be done with a loop but the point is to use a
recursive function.
"""
import requests


def recurse_help(pos, hot_list):
    """ A helper function - This function returns the list in reverse order.
    """
    if pos == -1:  # i.e the first list passed is empty
        return []
    if pos == 0:
        return list([hot_list[0]['data']['title']])
    returned = recurse_help(pos - 1, hot_list)
    return list([hot_list[pos]['data']['title']]) + returned


def recurse(subreddit):
    """ The function """
    my_client = requests.session()

    # Set custom `User-Agent` header to avoid "too many requests error (429)"
    my_client.headers['User-Agent'] = 'Another Custom User Agent for task 2'

    url = "https://www.reddit.com/r/{:s}/hot.json".format(subreddit)
    r = my_client.get(url, allow_redirects=False)
    if r.status_code == 200:
        children = r.json()['data']['children']
        result = recurse_help(len(children) - 1, children)
        return result
    else:
        return None
