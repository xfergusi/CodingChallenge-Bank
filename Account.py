class Account:

    money = 0
    
    def __init__(self, id):
        self.id = id

    def deposit(self, ammount):
        self.money = self.money + ammount
    
    def withdraw(self, ammount):
        self.money = self.money - ammount