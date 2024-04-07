from person import User,Admin
class Bank:
    def __init__(self,name) -> None:
        self.name = name
        self.users={}
        self.Admin=None
        self.Balance=0
        self.total_loan=0
        self.can_take_loan=True
    def add_user(self,name,uuser):
        self.users[name]=uuser
        
    def user_deposit_money(self,user_name,amount):
        self.users[user_name].balance+=amount
        self.users[user_name].Transection_history.append(f'{user_name}  have deposited money {amount }in his account , current balance {self.users[user_name].balance}')
        self.Balance += amount
    def user_available_balance(self,user_name):
        print(f'Available balance of {user_name} {self.users[user_name].balance}')
    def Transfer_money(self,sender,receiver,amount):
        self.users[sender].balance-=amount
        self.users[receiver].balance-= amount
        self.users[sender].Transection_history.append(f'{sender}  have sent money {amount }in {receiver}his account , current balance {self.users[sender].balance}')
        self.users[receiver].Transection_history.append(f'{receiver}  have received money {amount }in his account , current balance {self.users[receiver].balance}')
        
    def Loan_amount(self,name):
        if(name==self.Admin):
            print(f"total loan { self.total_loan}")
    def Current_balance(self,name):
        if(name==self.Admin):
            print(f"total Balance{ self.Balance}")
   
    
    def user_withdraw_money(self,user_name,amount):
        if self.users[user_name].balance >= amount:
            if self.Balance <amount:
                print("the bank is bankrupt")
            else:
                self.users[user_name].balance -= amount
                self.Balance-=amount
                self.users[user_name].Transection_history.append(f'{user_name}  have withdrawl money {amount }in his account , current balacne {self.users[user_name].balance}')
        
    def transection_history(self,name):
        for s in self.users[name].Transection_history:
            print(s)
    def Take_loan(self,name,loan):
        if self.users[name].balance*2>=loan and self.can_take_loan==True:
            self.Balance-=loan
            self.users[name].balance+=loan
            self.total_loan+=loan
    def loan_available(self,possible):
        self.can_take_loan=possible
        
    def add_admin(self,admin):
        self.Admin=admin
    
    
    

