class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

    def display(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.account_no)
        print("Account Holder :", self.holder_name)
        print("Balance :", self.balance)


account = BankAccount("123456789", "Saravana", 5000)

account.display()

deposit_amount = float(input("Enter Deposit Amount: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter Withdraw Amount: "))
account.withdraw(withdraw_amount)

account.display()