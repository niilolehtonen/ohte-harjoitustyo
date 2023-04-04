from logging import root
from register_view import RegisterView
from tkinter import Tk


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_RegisterView()

    def _show_RegisterView(self):
        self._current_view = RegisterView(self._root)

        self._current_view.pack()

window = Tk()
window.title("BudgetApp")

ui = UI(window)
ui.start()

window.mainloop()