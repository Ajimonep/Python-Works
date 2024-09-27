class Bank:
    def create_account(self,acno,acc_type):
        self.bank_name="SBI"
        self.__balance=2000
        self.acno=acno
        self.acc_type=acc_type


    def deposit(self,amount):
        self.__balance+=amount
        print(f"Your Acc {self.acno} is credited with amount {amount}")
     
        
    def withdraw(self,amount):

        if amount>self.__balance:
            print("Tranaction failed insufficient balance")

        else:

            self.__balance-=amount
            print(f"Your Acc {self.acno} is debited with amount {amount}")

    def get_balance(self):
        print(f"Your available balance is Rs{self.__balance}")


Bank_isntance=Bank()

Bank_isntance.create_account(1000,"saving")

Bank_isntance.deposit(5000)

Bank_isntance.withdraw(3000)

Bank_isntance.get_balance()

Bank_isntance.__balance+=2000