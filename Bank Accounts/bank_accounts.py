'''
This file contains all different classes for project.
Banking Account: This is basic class which contains all the parent attributes and methods.
InterestRewardAccount: Any deposit will get addidtional 5%.
SavingsAccount: Any withdrawl will result in reduction of 5%.
'''
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accountName):
        '''
        init method to create the account
        '''
        self.balance = initialAmount
        self.name = accountName
        with open(f'h:\quamtum computing\code practice\projects\Bank Account\{self.name}.txt', 'w') as file:
            # Determine the total line width
            total_width = 400  # Adjust this based on your needs

            text = '*******************WELCOME TO ABC BANK*******************'
            
            # Calculate the number of spaces needed to center the text
            padding = (total_width - len(text)) // 2

            # Create the centered text line
            title_line = ' ' * padding + text + ' ' * padding + '\n\n'

            file.write(title_line)
            file.write(f"Account Holder: {self.name}       Balance: {self.balance}\n\n")
            file.write(f"Action --> Amount($) --> Current Balance($)\n")
            print(f'File Created')
            file.close()
        print(f"Account created ! \nAccount: '{self.name}' with Balance: ${self.balance:.2f}\n")
    
    def getBalance(self):
        '''
        method: to get balance for a account
        '''
        print(f"Account: '{self.name}' and Balance: ${self.balance:.2f}\n")
        
    def deposit(self, amount):
        '''
        method: to deposit money in bank account
        '''
        self.balance += amount
        print(f"Deposit complete!")
        self.getBalance()
        with open(f'h:\quamtum computing\code practice\projects\Bank Account\{self.name}.txt', 'a') as file:
            file.write(f"Deposit --> {amount} --> {self.balance}\n\n")
        
    def viableTransaction(self, amount):
        '''
        method: to check if the account have enough balance or not!
        '''
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"The amount you entered is more than the available amount!\nAccount: '{self.name}', Available Balance: ${self.balance:.2f}\n"
            )
    
    def withdraw(self, amount):
        '''
        method: to deduct the withdrawl amount from the account
        '''
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"Withdrawl Complete!")
            self.getBalance()
            with open(f'h:\quamtum computing\code practice\projects\Bank Account\{self.name}.txt', 'a') as file:
                file.write(f"Withdrawl --> {amount} --> {self.balance}\n\n")
        except BalanceException as error:
            print(f"Withdrawl denied!\n{error}")
    
    def transfer(self, amount, account):
        '''
        method: to send a certain amount to a different account.
        '''
        try:
            print(f'******Transfer Begin...*******')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'******Transfer Complete...*******')
        except BalanceException as error:
            print(f"Transfer denied!\n{error}")
            print(f'******Transfer not complete...*******\n')
            
    def transactionHistory(self):
        '''
        method: to show the transaction history
        '''
        print(f"*********Transaction history for '{self.name}'*********")
        with open(f'h:\quamtum computing\code practice\projects\Bank Account\{self.name}.txt', 'r') as file:
            content = file.readlines()
            for line in content[:4:-1]:
                print(line)
        self.getBalance()

class InterestRewardAccount(BankAccount):
    '''
    This class is for a special type of Bank Account. 
    This class is a child class and parent class is BankAccount class.
    '''
    def deposit(self, amount):
        '''
        Here we are overriding the 'deposit' method. Any deposit made in this account will get an additional 5% interest.
        '''
        self.balance += (amount*1.05)
        print(f"Deposit Complete!")
        self.getBalance()
        with open(f'h:\quamtum computing\code practice\projects\Bank Account\{self.name}.txt', 'a') as file:
            file.write(f"Deposit --> {amount} --> {self.balance}\n\n")

class SavingsAccount(InterestRewardAccount):
    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)   # we are calling init of BankAccount class
        self.fee = 5
    
    def withdraw(self, amount):
        '''
        method: to deduct amount from the balance, additional $5 fee will also be deducted with every withdrawl.
        we are overriding the withdrawl method in grand parent class, i.e., Bank Account class.
        '''
        try:
            self.viableTransaction(amount+self.fee)
            self.balance -= (amount+self.fee)
            print(f"Withdrawl completed!")
            self.getBalance()
            with open(f'h:\quamtum computing\code practice\projects\Bank Account\{self.name}.txt', 'a') as file:
                file.write(f"Withdraw --> {amount} --> {self.balance}\n\n")
        except BalanceException as error:
            print(f"Withdrawl Denied!\n{error}")
