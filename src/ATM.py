class ATM:
    def __init__(self):
        self._balance = 0.0
        self._deposit_amount = 0.0
        self._withdraw_amount = 0.0

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, balance: float):
        self._balance = balance

    @property
    def deposit_amount(self) -> float:
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, deposit_amount: float):
        self._deposit_amount = deposit_amount

    @property
    def withdraw_amount(self) -> float:
        return self._withdraw_amount

    @withdraw_amount.setter
    def withdraw_amount(self, withdraw_amount: float):
        self._withdraw_amount = withdraw_amount
