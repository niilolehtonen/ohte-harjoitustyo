from tkinter import ttk, constants, StringVar

class BudgetView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label1 = ttk.Label(master=self._frame, text="Budget for this month")

        label1.grid(row=0, column=0)


    def pack(self):
        self._frame.pack(fill=constants.X)