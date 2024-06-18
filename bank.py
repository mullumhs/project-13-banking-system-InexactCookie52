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
bank = Bank()
bank.add_account("jhon", 1)
bank.add_account("jhon", 1)