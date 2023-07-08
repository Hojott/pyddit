""" Graphics with Custom Tkinter
"""

import customtkinter as ctk

class Window():
    """ Basic Window """

    def __init__(self) -> None:

        # Set default properties
        self._size = "1536x864" # 80% of 1920x1080

        # Set default theme
        self._appearance = "System"
        self._theme = "blue"
        ctk.set_appearance_mode(self.appearance)  # Modes: system (default), light, dark
        ctk.set_default_color_theme(self.theme)

        # Set window properties
        self._window = ctk.CTk()
        self._window.geometry(self.size)

    def __draw(self) -> None:
        """ Draw buttons etc. """
        pass

    async def create(self) -> None:
        """ Create new window """

        self.__draw()
        self._window.mainloop()


    # ===== Properties ===== #

    @property
    def size(self) -> str:
        """ Window size, in format '1920x1080' """
        return self._size

    @size.setter
    def size(self, size: str) -> bool:
        if "x" in size:
            self._size = size
            self._window.geometry(self.size)
            return True

        return False

    @property
    def appearance(self) -> str:
        """ Window appearance: dark, light and System """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance: str) -> bool:
        
        appearance = appearance.lower()

        if appearance in ["system", "light", "dark"]:
            if appearance == "system":
                # Fix System being capitalised for some reason
                self.appearance = "System"
            else:
                self._appearance = appearance
            ctk.set_appearance_mode(self.appearance)
            return True
        
        return False

    @property
    def theme(self) -> str:
        """ Window theme: blue, dark-blue and green """
        return self._theme

    @theme.setter
    def theme(self, theme: str) -> bool:
        if theme in ["blue", "green", "dark-blue"]:
            self._theme = theme
            ctk.set_default_color_theme(self.theme)
            return True

        return False


# ========================================================= #

if __name__=='__main__':
    window = Window()
    #window.create()
