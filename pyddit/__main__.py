#!/usr/bin/env python3
""" Pyddit - Python Client for Reddit
"""

from client import Client

def main():
    """ Run Pyddit Client """

    client = Client()
    client.start()

if __name__=='__main__':
    main()
