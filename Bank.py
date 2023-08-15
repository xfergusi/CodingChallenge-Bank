from Account import Account
class Bank:
    accounts = {}

    def create_account(self, id):
        self.accounts[id] = Account(id)
    
    def deposit(self, id, ammount):
        self.accounts[id].deposit(ammount)

    def show_ammount(self, id):
        print(self.accounts[id].money)

    def withdraw(self, id, ammount):
        self.accounts[id].withdraw(ammount)
        



    #     bank.deposit(1, 50)
    # bank.show_ammount(1)
    # bank.withdraw(1, 20)
    # bank.show_ammount(1)