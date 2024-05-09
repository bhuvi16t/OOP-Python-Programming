# ATM  SYSTEM BY USING OOP IN PYTHON :-
class Atm:

  def __init__(self):
     
     self.pin=''
     self.__balance=0
     self.menu()

  def menu(self):
     user_input =input("""
  >>> How can i help you ?
   1. press 1 for crete pin
   2. press 2 for change pin
   3. press 3 for check_balance
   4. press 4 for Withdraw
   5. press 5 for diposit 
   6. press 6 for exit() : """)
     
     if user_input=='1':
        self.create_pin()
     elif user_input=='2':
        self.change_pin()
     elif user_input=='3':
        self.check_balance()
     elif user_input=='4':
        self.withdraw()
     elif user_input=='5':
        self.deposit()
     else:
        exit()

  def create_pin(self ):
      
      user_pin=input('Enter a new pin :') 
      self.pin=user_pin
      usee_balance=input('enter your balance :') 
      self.__balance= usee_balance
      print('pin created  successfully')
      self.menu()

  def change_pin(self):
     
     old_pin=input('enter your old pin')
     new_pin=input('enter new pin')
     if old_pin==self.pin:
        self.pin=new_pin
        print("pin has been changed")
        self.menu()
     else:
        print('incorrect pin ')
        exit()

  def check_balance(self):
     security=input(' Enter your pin')
     if security==self.pin:
        print(f'Your current Balance is : {self.__balance}')
        self.menu()
     else:
        print('your are enter wromg pin')
        exit()
      
  def withdraw(self):
     withdraw_amount=int(input('Enter withdrawl Amount:'))
     security2=input('Enter your pin')
     if security2==self.pin:
        self.__balance=str(int(self.__balance) - int(withdraw_amount))
        print(f'{withdraw_amount} Is Debited from your account')
        print(f'Your current balance is : {self.__balance}')
        self.menu()
     else:
        print('iccorect pint ')

  def deposit(self):
     deposit_amount=input('Enter Deposit  Amount:')
     security3=input('Enter your pin')
     if security3==self.pin:
        self.__balance=str(int(self.__balance) + int(deposit_amount))
        print(f'{deposit_amount} Is Credit in your account')
        print(f'Your current balance is : {self.__balance}')
        self.menu()
     else:
        print('iccorect pin ')

  def get_balance(self):
     return self.__balance
  
  def set_balance(self ,new_value):
    if type(new_value)==int:
       self.__balance=new_value
    else:
       print('beta bahut pitooge')
     
       
obj=Atm()  
