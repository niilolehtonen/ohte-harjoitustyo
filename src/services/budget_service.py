from src.user import User
from src.repositories.user_repository import (user_repository as default_user_repository)

class InvalidCredentialsError(Exception):
    pass

class BudgetService:

    def __init__(self,user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def create_user(self, username, password):

        user = self._user_repository.create_user(User(username, password))

        return user

    def login(self,username,password):
        
        user = self._user_repository.search_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user


budget_service = BudgetService()