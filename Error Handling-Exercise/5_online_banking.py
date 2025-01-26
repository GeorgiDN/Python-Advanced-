class MoneyNotEnoughError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class PINCodeError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


MIN_AGE = 18


def validate_balance(amount, balance):
    if amount > balance:
        raise MoneyNotEnoughError("Insufficient funds for the requested transaction")


def validate_pin(pin_code, user_account_pin):
    if pin_code != user_account_pin:
        raise PINCodeError("Invalid PIN code")


def validate_age(age, min_age):
    if age < min_age:
        raise UnderageTransactionError("You must be 18 years or older to perform online transactions")


def validate_money(money):
    if money < 0:
        raise MoneyIsNegativeError("The amount of money cannot be a negative number")


def send_money(money, balance, pin_code, user_account_pin, age, min_age=MIN_AGE):
    validate_balance(money, balance)
    validate_pin(pin_code, user_account_pin)
    validate_age(age, min_age)
    print(f"Successfully sent {money:.2f} money to a friend")
    balance -= money
    print(f"There is {balance:.2f} money left in the bank account")
    return balance


def receive_money(money, balance):
    validate_money(money)
    amount_of_money = money / 2
    balance += amount_of_money
    print(f"{amount_of_money:.2f} money went straight into the bank account")
    return balance


def perform_transaction():
    user_account_pin, balance, age = list(map(int, input().split(", ")))

    while True:
        user_input = input().split("#")
        command = user_input[0]

        if command == "End":
            break

        money = int(user_input[1])

        if command == "Send Money":
            pin_code = int(user_input[2])
            balance = send_money(money, balance, pin_code, user_account_pin, age)

        elif command == "Receive Money":
            balance = receive_money(money, balance)


perform_transaction()
