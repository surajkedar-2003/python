#we can create our own exception class by inheriting from the built-in Exception class

class InSufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InSufficientBalanceError("Insufficient balance to withdraw the requested amount.")
    else:
        balance -= amount
        return balance


try:
    print(withdraw(1000, 1500))
except InSufficientBalanceError as error:
    print(error)