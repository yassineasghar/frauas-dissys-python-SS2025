# Exercise 3.1: Classes and Objects - Simple Bank Account


class BankAccount:
    def __init__(self, account_number: int, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        print(f'[ACC_NUM]: {self.account_number} | [DEPOSIT]: {amount}$')
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        print(f'[ACC_NUM]: {self.account_number} | [WITHDRAW]: {amount}$')
        self.balance -= amount

    def print_balance(self) -> None:
        print(f'[ACC_NUM]: {self.account_number} | [BALANCE]: {self.balance}$')


def main() -> None:
    bank_account = BankAccount(account_number=723564, balance=100)
    bank_account.print_balance()
    bank_account.deposit(100)
    bank_account.print_balance()
    bank_account.withdraw(50)
    bank_account.print_balance()


if __name__ == '__main__':
    main()
