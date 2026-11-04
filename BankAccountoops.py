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
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance=0,rate=2):
        super().__init__(owner,balance)
        self.rate=rate
    def Intrest(self):
        intrest = self.balance*self.rate/100
        print(f'intrest of a rate {self.rate}%,on a balance {self.balance}Rs is: {self.balance+intrest}')
# acc = BankAccount('Sajad', 100)
sav = SavingsAccount('Sajad', 1000, 5)

# acc.withdraw(50)
# print(acc.balance)    # 50  — bank form dropped
print(sav.balance)    # 1000 — savings form untouched
print(sav.show())
print(sav.rate)
sav.Intrest()
# #test case
# acc = BankAccount('Sajad', 10000)
# acc.deposit(50)
# acc.withdraw(30)
# acc.withdraw(10000)
# acc.show()
# #testCase
# sav = SavingsAccount('Sajad', 1000)
# sav.deposit(50)  # we never wrote deposit or withdrawl in  here... yet it works
# sav.show()           # Sajad: 1050

