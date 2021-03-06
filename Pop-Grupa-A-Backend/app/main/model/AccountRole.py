from enum import Enum

class AccountRole(Enum):
    ADMIN = 1
    APP_USER = 2
    SUPPLIER = 3
    SCHEDULER = 4

    def __str__(self):
        return self.name
