from tkinter import ttk, constants, StringVar
import os, sys
dir = os.path.dirname("budget_service.py")
sys.path.append(dir)
from src.services.budget_service import budget_service
class RegisterView:
    def __init__(self, root, handle_create_account, handle_show_LoginView):
        self._root = root
        self._handle_create_user = handle_create_account
        self._handle_show_login_view = handle_show_LoginView
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def _create_account_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        budget_service.create_user(username=username,password=password)
        self._handle_create_user()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame,show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        button_register = ttk.Button(master=self._frame,text="Register",command=self._create_account_handler)

        button_login = ttk.Button(master=self._frame,text="Back to Login",command=self._handle_show_login_view)

        self._initialize_username_field()
        self._initialize_password_field()

        button_register.grid(padx=5, pady=5, sticky=constants.W)
        button_login.grid(padx=5, pady=5, sticky=constants.W)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

    def pack(self):
        self._frame.pack(fill=constants.X)