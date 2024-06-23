""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from account import Account
class Bank:
    def __init__(self):
        self._accounts = []

    def acc_exists(self, acc_num):
        for i in self._accounts:
            if i.get_acc_num() == acc_num:
                return i
        return False
        

    def add_account(self, name, acc_num):
        if self.acc_exists(acc_num) is False:
            new_account = Account(name, acc_num)
            self._accounts.append(new_account)
            print(f"account, {name} has been added:")
        else:
            print(f"account {name}, already exists: ")

    def del_acc(self, acc_num):
        account = self.acc_exists(acc_num)
        if account:
            self._accounts.remove(account)
            print(f"Account deleted")
        else:
            raise ValueError(f"Account {acc_num}, not found")
        

    def deposit(self, acc_num, amount):
        account = self.acc_exists(acc_num)
        if account:
           account.deposit(amount)
           print(f"You deposited ${amount}")
        else:
            raise ValueError(f"Account {acc_num}, not found")
        
    def withdraw (self, acc_num, amount):
        account = self.acc_exists(acc_num)
        if account: #and self.get_balance(acc_num) >= amount
           account.withdraw(amount)
           print(f"You withdrew ${amount}, your new balance is ${account.get_balance()}")
        else:
            raise ValueError(f"Account {acc_num}, not found")
    
    
bank = Bank()
bank.add_account("jhon", 1)
bank.add_account("JANE", 2)
bank.add_account("jhon", 1)
bank.del_acc(2)
bank.deposit(1,100)
bank.withdraw(1, 20)