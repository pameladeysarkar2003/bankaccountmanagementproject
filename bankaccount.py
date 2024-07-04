class BankAccount:
    def__init__(self,initialAmount,accName):
    self.balance=initialAmount
    self.name=acctName
    print(f"\nAccount '{self.name}' created.\nBaance=${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount'{self.name}' balance=${self.balance:.2f}")

        def deposit(self,amount):
            self.balnce=self.balance+amount
            print("\nDeposit complete.")
            self.getBalance()

            def viableTransaction(self,amount):
                if self.balance>=amount:
                    return
                else:
                    raise BalanceException(
                        f"\nSorry,account '{self.name}' only has a balance of ${self.balance:.2f}"
                    )
                
                def withdraw(self,amount):
                    try:
                        self.variableTRansaction(amount)
                        self.balance=self.balance-amount
                        print("\nWithdraw complete.")
                        self.getBalance()
                    except BalanceException as error:
                        print(f'\nWithdraw interrupted:{error}')
              
