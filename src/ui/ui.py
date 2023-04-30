from logging import root
from register_view import RegisterView
from login_view import LoginView
from budget_view import BudgetView
from tkinter import Tk


class UI:
    """Class responsible for the whole UI.

    Attributes: TKinter element where the view will be initialized.
    """
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        """Starts the application.
        """

        self._show_LoginView()
        #self._show_BudgetView()

    def _show_RegisterView(self):
        """Shows the register window.
        """

        self._hide_current_view()

        self._current_view = RegisterView(self._root, self._show_RegisterView, self._show_LoginView)

        self._current_view.pack()
    
    def _show_LoginView(self):
        """Shows the login window.
        """

        self._hide_current_view()

        self._current_view = LoginView(self._root, self._show_BudgetView, self._show_RegisterView)

        self._current_view.pack()

    def _show_BudgetView(self):
        """Shows the budget window.
        """

        self._hide_current_view()

        self._current_view = BudgetView(self._root, self._show_LoginView)

        self._current_view.pack()

    def _hide_current_view(self):
        """Method for hiding the current window, used when switching between windows.
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

window = Tk()
window.title("BudgetApp")

ui = UI(window)
ui.start()

window.mainloop()
