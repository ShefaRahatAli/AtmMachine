from abc import ABC, abstractmethod

class AtmOperationInterface(ABC):
    @abstractmethod
    def view_balance(self):
        pass

    @abstractmethod
    def withdraw_amount(self, withdraw_amount: float):
        pass

    @abstractmethod
    def deposit_amount(self, deposit_amount: float):
        pass

    @abstractmethod
    def view_mini_statement(self):
        pass