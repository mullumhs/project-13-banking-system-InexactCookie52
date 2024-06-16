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

    def add_account(self, name, acc_num):
        for account in self._accounts:
            if account.name == name:
                print(f"account, {account.name} already exits")
                return
            new_account = Account(name, acc_num)
            self._accounts.append(new_account)
            print(f"axccount, {account.name} has been added:")
        