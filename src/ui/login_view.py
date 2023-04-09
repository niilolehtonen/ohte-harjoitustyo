from tkinter import ttk, constants, StringVar

class LoginView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label1 = ttk.Label(master=self._frame, text="Login")
        
        username_var = StringVar()
        username_label = ttk.Label(master=self._frame, text="Username:")
        username_entry = ttk.Entry(master=self._frame, text="")

        password1_label = ttk.Label(master=self._frame,text="Password:")
        password1_entry = ttk.Entry(master=self._frame,text="",show="*")

        button_login = ttk.Button(master=self._frame,text="Login")
        button_create= ttk.Button(master=self._frame,text="Create an account")


        label1.grid(row=0, column=0)
        username_label.grid(row=2, column=0)
        username_entry.grid(row=2, column=1)
        password1_label.grid(row=3, column=0)
        password1_entry.grid(row=3, column=1)
        button_login.grid(row=5, column=0)
        button_create.grid(row=5, column=1)

    def pack(self):
        self._frame.pack(fill=constants.X)