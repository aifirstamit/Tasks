## Build a payment-processing example with an abstract Payment class containing a pay() method.

from abc import ABC, abstractmethod


class Payment(ABC):
    """Abstract base class for payment processing."""

    @abstractmethod
    def pay(self, amount):
        """Process a payment."""
        pass


class CreditCardPayment(Payment):
    """Process payment using a credit card."""

    def pay(self, amount):
        print("Processing Credit Card payment...")
        print("Amount Paid:", amount)


class UPIPayment(Payment):
    """Process payment using UPI."""

    def pay(self, amount):
        print("Processing UPI payment...")
        print("Amount Paid:", amount)


class NetBankingPayment(Payment):
    """Process payment using Net Banking."""

    def pay(self, amount):
        print("Processing Net Banking payment...")
        print("Amount Paid:", amount)


# Create different payment objects

credit_card = CreditCardPayment()
upi = UPIPayment()
net_banking = NetBankingPayment()


# Runtime polymorphism

print("===== Credit Card Payment =====")
credit_card.pay(5000)

print("\n===== UPI Payment =====")
upi.pay(2500)

print("\n===== Net Banking Payment =====")
net_banking.pay(7500)


# Demonstrate polymorphism using a loop

print("\n===== Runtime Polymorphism =====")

payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

for payment in payments:
    payment.pay(1000)