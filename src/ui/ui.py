from logging import root
from register_view import RegisterView
from login_view import LoginView
from budget_view import BudgetView
from tkinter import Tk


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_LoginView()
        #self._show_BudgetView()

    def _show_RegisterView(self,):
        self._hide_current_view()

        self._current_view = RegisterView(self._root, self._show_RegisterView, self._show_LoginView)

        self._current_view.pack()
    
    def _show_LoginView(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root, self._show_BudgetView, self._show_RegisterView)

        self._current_view.pack()


    def _show_BudgetView(self):
        self._hide_current_view()

        self._current_view = BudgetView(self._root, self._show_LoginView)

        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

window = Tk()
window.title("BudgetApp")

ui = UI(window)
ui.start()

window.mainloop()