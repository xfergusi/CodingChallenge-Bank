from Bank import Bank

def main():
    bank = Bank()
    bank.create_account(1)
    
    bank.deposit(1, 50)
    bank.show_ammount(1)
    bank.deposit(1, 55)
    bank.show_ammount(1)
    bank.withdraw(1, 20)
    bank.show_ammount(1)

if __name__ == "__main__":
    main()