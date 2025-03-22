class ATM:
    def __init__(self):
        self.balance = 0
        self.mini_statement = {}


    def view_balance(self):
        print(f"Available Balance: {self.balance}")

    def withdraw_amount(self, amount):
        if amount % 500 == 0:
            if amount <= self.balance:
                self.mini_statement[amount] = "Amount Withdrawn"
                print(f"Collect the Cash: {amount}")
                self.balance -= amount
                self.view_balance()
            else:
                print("Insufficient Balance!!")

        else:
            print("Please enter the amount in multiple of 500")
    

    def deposit_amount(self, amount):
        self.mini_statement[amount] = "Amount Deposited"
        print(f"{amount} Deposited Succefully..!!")
        self.balance += amount
        self.view_balance()

    def view_mini_statement(self):
        for key, value in self.mini_statement.items():
            print(f"{key} {value}")



    def main():
        atm = ATM()
        correct_atm_number = 123467
        correct_piun = 9876

        print("Welcome to ATM Machine !!!")
        atm_number = int(input("Enter ATM Number: "))
        pin = int(input("Enter PIN: "))

        if atm_number == correct_atm_number and pin == correct_pin:
            while True:
                print("\n1. View Available Balance\n2. Withdraw Amount\n3. Deposit Amount\n4. View Mini Statement\n5. Exit")
                choice = int(input("Enter Choice: "))

                if choice == 1:
                    atm.view_balance()
                elif choice == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    atm.withdraw_amount(amount)
                elif choice == 3:
                    amount = float(input("Enter amount to deposit: "))
                    atm.deposit_amount(amount)
                elif choice == 4:
                    atm.view_mini_statement()
                elif choice == 5:
                    print("Collect your ATM Card\nThank you for using ATM Machine!!")
                    break
                else:
                    print("Please enter a correct choice")
        else:
            print("Incorrect ATM Number or PIN")
        

if __name__ == "__main__":
    main()
