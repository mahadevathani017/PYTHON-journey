class BankAccount:
    def __init__(self,balance=0):
        self.balances=balance

    def withdraw(self,amount):
        if self.balances>=amount:
            self.balances-=amount
            print(f"{amount} with draw successfully")
        else:
            print("Not enough balance")
    def deposit(self,amount):
        slef.balances+=amount
        print(f"{amount} successfully deposited")
    def balance(self):
        print(f"The balance is {self.balances}")
account=BankAccount(int(input("Enter the opening balance:")))
loop_runner=True

while loop_runner:
    print("\nBankAccount")
    print("Operations\n 1. Withdraw\n 2. Deposite \n 3. Balance \n 4. To Exit")
    option = int(input("Choice: "))
    
    if option==1:
        account.withdraw(int(input("Enter the amount")))
    elif option==2:
        account.deposit(int(input("Enter the amount:")))
    elif option ==3:
        account.balance()
    else:
        loop_runner=False


       

