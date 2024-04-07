from Bank import Bank
from person import User,Admin
def main():
#creating Bank
    MyBank = Bank('Rupali Bank')
#Creating User
    Rahim = User('Rahim23@gmail.com',1234)
    MyBank.add_user('Rahim',Rahim)
    Fahim = User('Fahim33@gmail.com',4321)
    MyBank.add_user('Fahim',Fahim)
    
#Deposit money
    MyBank.user_deposit_money('Rahim',5000)
    MyBank.user_deposit_money('Fahim',10000)
    MyBank.user_withdraw_money('Rahim',1000)
#Check Available Balance
    MyBank.user_available_balance('Fahim')
#Transfer Money
    MyBank.Transfer_money('Fahim','Rahim',500)
#take loan
    MyBank.Take_loan('Fahim',2000)

#Creating Admin
    
    Aadmin = Admin('Admin22@gmail.com',9923)
    MyBank.add_admin(Aadmin)
#can disable loan taking option
    MyBank.loan_available(False)
# check total loan amount
    MyBank.Loan_amount(Aadmin)
#  check total balance 
    MyBank.Current_balance(Aadmin)


# call the main 
if __name__ == '__main__':
    main()