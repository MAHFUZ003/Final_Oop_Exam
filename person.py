class Person:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password


class User(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.balance = 0
        self.Transection_history = []


class Admin(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
