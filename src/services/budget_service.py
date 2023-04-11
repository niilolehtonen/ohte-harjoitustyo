from user import User
from repositories.user_repository import (user_repository as default_user_repository)


class BudgetService:

    def __init__(self,user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository