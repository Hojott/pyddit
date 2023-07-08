""" Authentication graphics
"""

from . import Window
import customtkinter as ctk

# Debug
import asyncio

class AuthenticationWindow(Window):
    """ First Window asking for authentication """
    def __init__(self) -> None:
        super().__init__()

    def login(self):
        pass

    def __draw(self) -> None:
        button = ctk.CTkButton(master=self._window, text="Log in", command=self.login)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    async def create(self):
        self.__draw()
        self._window.mainloop()
    
# =======================================#

async def main():
    window = AuthenticationWindow()
    await window.create()
    await asyncio.sleep(5)
    window.appearance = "light"

if __name__ == '__main__':
    asyncio.run(main())
