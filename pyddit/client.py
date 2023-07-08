""" Pyddit Client
"""

from graphics.authentication import AuthenticationWindow

import asyncio

class Client():
    """ Pyddit client """
    def __init__(self):
        pass

    def start(self):
        auth_window = AuthenticationWindow()
        return asyncio.run(auth_window.create())

