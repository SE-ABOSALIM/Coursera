from abc import ABC, abstractmethod


# 1. Strategy
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# 2. Concrete Strategies
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")


class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")


class BankTransferPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using Bank Transfer.")


# 3. Context
class Payment:

    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# 4. Usage

credit_card = CreditCardPayment()
payment = Payment(credit_card)
payment.make_payment(100)

print("----------------")

paypal = PayPalPayment()
payment = Payment(paypal)
payment.make_payment(200)

print("----------------")

bank_transfer = BankTransferPayment()
payment = Payment(bank_transfer)
payment.make_payment(300)