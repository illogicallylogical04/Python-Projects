from bank_accounts import *

Dave = BankAccount(1000, 'Dave')
Dave.deposit(1000)

Sara = BankAccount(2000, 'Sara')

Dave.getBalance()
Sara.getBalance()

Dave.deposit(1000)

Dave.withdraw(50)

#Dave.transfer(20000, Sara)

Jim = InterestRewardAccount(1000, 'Jim')
Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAccount(1000, 'Blaze')
Blaze.deposit(100)
Blaze.transfer(10000, Sara)

Dave.withdraw(50)
Dave.transactionHistory()