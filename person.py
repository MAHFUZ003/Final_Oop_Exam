class Person:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password


class User(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.balance = 0
        self.Transection_history = []
    def trans_histry(self):
        for s in self.Transection_history:
            print(s)

        


class Admin(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
