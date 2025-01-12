# user_management/repository.py
from typing import Optional
from user_management.models import User

class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User) -> None:
        if user.username in self.users:
            raise ValueError("Username already exists")
        self.users[user.username] = user

    def find_user_by_username(self, username: str) -> Optional[User]:
        return self.users.get(username)