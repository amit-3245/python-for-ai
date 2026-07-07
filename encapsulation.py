# Encapsulation : wrapping data and functions into single unit

# public : accessable everywhere
# protected attributes: its accessable inside class and subclass
#private attributes: accessable only inside the class

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance # protected attributes because here use _ after .

    def get_balance(self):#getter
        return self._balance

    def set_balance(self, NewBalance): #setter
        self._balance = newBalance

acc1 = BankAccount("Amit", 100000)
print(acc1.name, acc1.balance)

acc1.set_balance(200000)

#access private variable
print(acc1.name)