class Transaction:
    """This class represents a transaction object, the transaction can be an expense or an income.

    Attributes:
        username: Using username as an identifier for the transaction.
        type: Defines the transaction type (income or expense).
        name: Name/description for the transaction.
        amount: Amount of transaction (integer value).
    """

    def __init__(self,username,type,name,amount):
        self.username = username
        self.type = type # Expense or Income
        self.name = name
        self.amount = amount
