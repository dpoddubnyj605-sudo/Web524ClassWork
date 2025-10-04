class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f"{self.owner} пополнил счёт на {amount}. Новый баланс: {self.balance}")

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Процентная ставка изменена на {cls.interest_rate}")

    @staticmethod
    def is_valid_amount(amount):
        if (isinstance(amount, int) or isinstance(amount, float)) and amount > 0:
            #                   True                                 True
            return True
        raise ValueError('Сумма пополнения должна быть положительным числом')


if __name__ == '__main__':
    account = BankAccount('Иван', 1000)
    account.deposit(500)
    BankAccount.set_interest_rate(0.07)
    # print(BankAccount.is_valid_amount(600.50))
    # print(BankAccount.is_valid_amount(600))
    account.deposit(600.50)

