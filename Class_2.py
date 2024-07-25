# Create account class with 2 attributes - balance and account no.
# Create Methods for debit, credit and printing the balance.

class Account():
    
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    
    def print_balance(self):
        print('Your account balance is :', self.balance)

    def debit(self,withdraw):
        if withdraw>self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= withdraw
            print(f'Amount you have withdrawan {withdraw}. Your new balance is {self.balance}')

    def credit(self,deposit):
        self.balance += deposit
        print(f'you have deposited {deposit}. Your new balance is {self.balance}')


s1 = Account(5000, 123)
        
s1.print_balance()  
s1.debit(2000)      
s1.credit(1500)      
s1.print_balance() 

