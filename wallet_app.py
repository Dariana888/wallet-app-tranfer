class Wallet:
    def __init__(self, money=0):
        self.money = money

    def add_money(self, amount):
        if amount > 0:
            self.money += amount
    def withdraw(self,amount):
        if amount <= self.money:
            self.money -= amount
        else:
            print('Fonduri insuficiente pentru transfer')
    def transfer(self, other_wallet, amount):
        if amount <= self.money:
            self.money -= amount
            other_wallet.money += amount

my_wallet = Wallet()
my_wallet.add_money(300)
my_wallet.add_money(150)
my_wallet.add_money(500)


class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()

user = User('Ana')
user.wallet.add_money(300)
print(user.wallet.money)

user2 = User('Mihai')
user2.wallet.add_money(150)
print(user2.wallet.money)

user3 = User('Dumitru')
user3.wallet.add_money(500)
print(user3.wallet.money)

w1 = Wallet(300)
w2 = Wallet(150)
w3 = Wallet(500)
w1.transfer(w2, 100)
w3.transfer(w1,200)
w2.transfer(w3,50)

print(w1.money)
print(w2.money)
print(w3.money)