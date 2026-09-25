## Question: Create a simplified banking application using Python OOP.

class BankAccount:

    # Class variables
    bank_name = "ABC Bank"
    total_accounts = 0

    # Constructor
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

        # Increase total account count
        BankAccount.total_accounts += 1

    # Instance method
    def deposit(self, amount):
        """Add money to the account."""

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount

        print("Deposit successful.")
        print("Deposited:", amount)

    # Instance method
    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available."""

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount

        print("Withdrawal successful.")
        print("Withdrawn:", amount)

    # Instance method
    def check_balance(self):
        """Display the current account balance."""

        print("Current Balance:", self.balance)

    # Instance method
    def display_account_details(self):
        """Display account details."""

        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Bank Name:", BankAccount.bank_name)
        print("Balance:", self.balance)

    # Class method
    @classmethod
    def change_bank_name(cls, new_bank_name):
        """Change the bank name for all accounts."""

        cls.bank_name = new_bank_name

    # Class method
    @classmethod
    def get_total_accounts(cls):
        """Return the total number of bank accounts."""

        return cls.total_accounts


# Create bank account objects

account1 = BankAccount(
    "Aman",
    "ACC101",
    10000
)

account2 = BankAccount(
    "Ravi",
    "ACC102",
    15000
)


# Display account details

print("===== Account 1 =====")
account1.display_account_details()

print("\n===== Account 2 =====")
account2.display_account_details()


# Deposit money

print("\n===== Deposit =====")

account1.deposit(5000)

account1.check_balance()


# Withdraw money

print("\n===== Withdrawal =====")

account1.withdraw(3000)

account1.check_balance()


# Test insufficient balance

print("\n===== Insufficient Balance Test =====")

account1.withdraw(50000)


# Change bank name

print("\n===== Changing Bank Name =====")

BankAccount.change_bank_name("XYZ Bank")

print("Account 1 Bank:", BankAccount.bank_name)
print("Account 2 Bank:", BankAccount.bank_name)


# Total accounts

print("\n===== Total Bank Accounts =====")

print("Total Accounts:", BankAccount.get_total_accounts())