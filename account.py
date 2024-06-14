""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Account:
    def __init__(self, name, acc_num):
        self._set_name(name)
        self._set_acc_num(acc_num)
        self._balance = 0

    def get_name(self):
        return self._name
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name != "":
            self._name = new_name
        else:
            raise ValueError("Name is not a string: ")
    def get_acc_num(self):
        return self._acc_num
    def set_acc_num(self, new_acc_num):
        if isinstance(new_acc_num, int) and new_acc_num != "":
            self._acc_num = new_acc_num
        else:
            raise ValueError("Acc_num is not an int: ")

    def get_balance(self):
        return self._balance
    def set_balance(self, new_balance):
        if isinstance(new_balance, float) and new_balance != "":
            self._balance = new_balance
        else:
            raise ValueError("balance is not a float: ")
        

    def withdraw()