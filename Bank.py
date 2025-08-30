# Bank Class
# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details. Give the complete code for the BankAccount class.

# write your code here

class Bank :
  
  # contrsuctor 
  def __init__(self,AccoutNumber,Name,Amount) :
    self.AccoutNumber=AccoutNumber
    self.Name=Name
    self.Amount=Amount
  
  # deposit method
  def deposit(self,DepoAmount):

    self.Amount = self.Amount + DepoAmount
    print('your Amount credit successfully ')
    print('Current Balance is :',self.Amount)

  # withdrawl method 
  def withdrawl(self,withAmount):
    if withAmount < self.Amount:
      self.Amount -= withAmount
      print(f'RS{withAmount} Debited from your Account your available  balance is {self.Amount}')
 # display method 
  def Display(self):
    print(f'Account Number : {self.AccoutNumber}')
    print(f'Account Name : {self.Name}')
    print(f'Account Balance : {self.Amount}')

New_Accout= Bank(1234564,'Bhoopendra',500000)
New_Accout.withdrawl(10000)
New_Accout.deposit(15000)
New_Accout.Display()
