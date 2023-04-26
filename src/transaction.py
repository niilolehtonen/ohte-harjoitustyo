class Transaction:

    def __init__(self,username,type,name,amount):
        self.username = username
        self.type = type # Expense or Income
        self.name = name
        self.amount = amount
