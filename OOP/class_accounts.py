import datetime
import pytz


class Account:
    """Simple account class with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        print("Account created for " + self._name)
        self._transaction_list.append((Account._current_time(), balance, self.__balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount, self.__balance))
    def withdraw(self, amount):
        if self.__balance >= amount > 0:
            self.__balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount, self.__balance))
        else:
            print("Insufficient funds")

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount, balance in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} - Local time was {}".format(amount, tran_type, date, date.astimezone()))
            print("Current balance: {}".format(balance))
if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()
    tim.show_transactions()

    daniel = Account("Daniel", 800)
    daniel.deposit(100)
    daniel.withdraw(200)
    daniel.show_transactions()

    print(daniel.__dict__)