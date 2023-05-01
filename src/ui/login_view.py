from tkinter import ttk, constants, StringVar
import os, sys
dir = os.path.dirname("budget_service.py")
sys.path.append(dir)
from src.services.budget_service import budget_service, InvalidCredentialsError

class LoginView:
    """Class for the UI of the register window.

    Attributes:
        root: TKinter element where the view will be initialized.
        handle_login: Value that is called when logging in.
        handle_show_RegisterView: Value that is called when switching to register view.
    """

    def __init__(self, root, handle_login, handle_show_RegisterView):
        self._root = root
        self._frame = None
        self._handle_show_create_user_view = handle_show_RegisterView
        self._handle_login = handle_login

        self._initialize()

    def destroy(self):
        """Destroys the frame.
        """

        self._frame.destroy()


    def _login_handler(self):
        """On-click functionality for the login button.
        """

        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            budget_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._show_error("Invalid username or password")

    def _initialize_username_field(self):
        """Initializes username entry field.
        """

        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        """Initializes password entry field.
        """

        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        """Initializes the view.
        """

        self._frame = ttk.Frame(master=self._root)
        label1 = ttk.Label(master=self._frame, text="Login")
        

        button_login = ttk.Button(master=self._frame,text="Login",command=self._login_handler)
        button_create= ttk.Button(master=self._frame,text="Create an account",command=self._handle_show_create_user_view)

        self._initialize_username_field()
        self._initialize_password_field()

        label1.grid(row=0, column=0)

        button_login.grid(padx=5, pady=5, sticky=constants.EW)
        button_create.grid(padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

    def pack(self):
        """Shows the frame.
        """

        self._frame.pack(fill=constants.X)
