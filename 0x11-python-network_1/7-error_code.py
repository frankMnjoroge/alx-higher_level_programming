#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    url = argv[1]
    resp = get(url)
    error_txt = 'Error code: {}'
    status = resp.status_code
    print(error_txt.format(status) if (status >= 400) else resp.text)
