class Transaction:

    def __init__(self,user_id,type,name,amount):
        self.user_id = user_id
        self.type = type # Expense or Income
        self.name = name
        self.amount = amount

