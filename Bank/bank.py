class Bank:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        while True:
            user_input = int(input("""
            Hello, how would you like to proceed?
            1. To Create a pin press 1
            2. To Deposit Cash press 2
            3. To Withdraw Cash press 3
            4. To Check Balance press 4
            5. To exit press 5
            """))




            
            
            if user_input == 1:
                self.create_pin()
                
            elif user_input == 2:
                self.deposit()
                
            elif user_input == 3:
                self.withdraw()
                
            elif user_input == 4:
                self.check_balance()
            else:
                print("Bye")
                exit()

    def create_pin(self):
        self.pin = input("Enter the pin you want to create: ")
        print("Pin Created Successfully")
    
    def deposit(self):
        pin = input("Enter your pin: " )
        if self.pin == pin:
            amount = int(input("enter the amount: "))
            self.balance += amount
            print("Cash Deposit Successfully")
        else:
            print("invalid pin")
    def withdraw(self):
        pin = input("Enter your pin: " )
        if self.pin == pin:
            amount = int(input("enter the amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Cash Withdraw Successfully")
            else:
                print("Insufficient balance")
        else:
            print("invalid pin")
    def check_balance(self):
        pin = input("Enter your pin: " )
        if pin == self.pin:
            print("your balance is: ",self.balance)
        else:
            print("invalid pin")



SBI = Bank()


            

     