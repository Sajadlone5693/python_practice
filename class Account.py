class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner= owner
        self.balance= balance
    def deposit(self,amount):
        self.balance +=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -=amount
        else:
            print('low balance')

    def show(self):
        print(f'{self.owner}:{self.balance}')

#test case
acc = BankAccount('Sajad', 10000)
# acc.deposit(50)
# acc.withdraw(30)
acc.withdraw(10001)
acc.show()