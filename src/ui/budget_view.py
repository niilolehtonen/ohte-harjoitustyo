from tkinter import ttk, Listbox, END
from src.services.budget_service import budget_service

class BudgetView:
    def __init__(self, root, handle_show_LoginView):
        self._root = root
        self._frame = None
        self._handle_show_LoginView = handle_show_LoginView


        self._initialize()

    def destroy(self):
        self._frame.destroy()
    def _update_budget_label(self):
        budget = budget_service.show_budget()[0]
        self._budget_label.config(text=f'{budget}e')

    def _handle_new_income(self):
        income_a = self._new_income_amount_entry.get()
        income_n = self._new_income_name_entry.get()
        budget_service.new_income(income_n, income_a)
        show_budget = budget_service.show_budget()
        self._update_budget_label()
        self._income_listbox.delete(0, END)
        for income in show_budget[2]:
            self._income_listbox.insert(END, f"{income.name}: {income.amount}e")

    def _handle_new_expense(self):
        expense_a = self._new_expense_amount_entry.get()
        expense_n = self._new_expense_name_entry.get()
        budget_service.new_expense(expense_n, expense_a)
        show_budget = budget_service.show_budget()
        self._update_budget_label()
        self._expense_listbox.delete(0, END)
        for expense in show_budget[1]:
            self._expense_listbox.insert(END, f"{expense.name}: {expense.amount}e")

    def _initialize_budget(self):
        show_budget = budget_service.show_budget()
        budget = show_budget[0]

        for income in show_budget[2]:
            self._income_listbox.insert(END, f"{income.name}: {income.amount}e")

        for expense in show_budget[1]:
            self._expense_listbox.insert(END, f"{expense.name}: {expense.amount}e")

        self._budget_label = ttk.Label(master=self._frame,text=f'{budget}e')
        self._budget_label.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
        )

    def _logout_handler(self):
        budget_service.logout()
        #self._handle_logout()
        self._handle_show_LoginView()

    def _initialize_footer(self):
        self._new_expense_amount_entry = ttk.Entry(master=self._frame)
        self._new_expense_name_entry = ttk.Entry(master=self._frame)
        self._new_income_amount_entry = ttk.Entry(master=self._frame)
        self._new_income_name_entry = ttk.Entry(master=self._frame)

        self._name_label_i = ttk.Label(master=self._frame,text="Name:")
        self._amount_label_i = ttk.Label(master=self._frame,text="Amount:")
        self._name_label_e = ttk.Label(master=self._frame,text="Name:")
        self._amount_label_e = ttk.Label(master=self._frame,text="Amount:")

        new_expense_button = ttk.Button(
            master=self._frame,
            text="New expense",
            command=self._handle_new_expense
        )

        new_income_button = ttk.Button(
            master=self._frame,
            text="New income",
            command=self._handle_new_income
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        self._income_listbox = Listbox(master=self._frame)
        self._expense_listbox = Listbox(master=self._frame)

        self._amount_label_i.grid(row=2, column=2, padx=5, pady=5)
        self._new_income_amount_entry.grid(row=3, column=2, padx=5, pady=5)
        self._name_label_i.grid(row=4, column=2, padx=5, pady=5)
        self._new_income_name_entry.grid(row=5, column=2, padx=5, pady=5)
        new_income_button.grid(row=6, column=2, padx=5, pady=5)
        self._income_listbox.grid(row=7, column=2, padx=5, pady=5)

        self._amount_label_e.grid(row=2, column=0, padx=5, pady=5)
        self._new_expense_amount_entry.grid(row=3, column=0, padx=5, pady=5)
        self._name_label_e.grid(row=4, column=0, padx=5, pady=5)
        self._new_expense_name_entry.grid(row=5, column=0, padx=5, pady=5)
        new_expense_button.grid(row=6, column=0, padx=5, pady=5)
        self._expense_listbox.grid(row=7, column=0, padx=5, pady=5)
        logout_button.grid(row=8, column=1, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label1 = ttk.Label(master=self._frame, text="Budget for this month")

        label1.grid(row=0, column=1)

        self._initialize_footer()
        self._initialize_budget()

        self._frame.grid_rowconfigure(7, weight=1, minsize=50)
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=1, minsize=400)
        self._frame.grid_columnconfigure(2, weight=1, minsize=400)

    def pack(self):
        self._frame.pack()
