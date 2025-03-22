class ATM:
    def __init__(self):
        self._balance = 0.0
        self._mini_statement = {}

    def view_balance(self):
        print(f"Available Balance is: {self._balance}")

    def withdraw_amount(self, withdraw_amount: float):
        if withdraw_amount % 500 == 0:
            if withdraw_amount <= self._balance:
                self._mini_statement[withdraw_amount] = " Amount Withdrawn"
                print(f"Collect the Cash {withdraw_amount}")
                self._balance -= withdraw_amount
                self.view_balance()
            else:
                print("Insufficient Balance !!")
        else:
            print("Please enter the amount in multiples of 500")

    def deposit_amount(self, deposit_amount: float):
        self._mini_statement[deposit_amount] = " Amount Deposited"
        print(f"{deposit_amount} Deposited Successfully !!")
        self._balance += deposit_amount
        self.view_balance()

    def view_mini_statement(self):
        for amount, transaction in self._mini_statement.items():
            print(f"{amount} {transaction}")


# Example usage
atm = ATM()
atm.deposit_amount(2000)
atm.withdraw_amount(500)
atm.view_mini_statement()
