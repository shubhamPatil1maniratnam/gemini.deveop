class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid or insufficient funds.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")

def main():
    print("=== Welcome to Simple Bank ===")
    account_number = input("Enter account number: ")
    holder_name = input("Enter account holder name: ")
    account = BankAccount(account_number, holder_name)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input.")
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using Simple Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
