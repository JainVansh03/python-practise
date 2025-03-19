**BankSystem**


Purpose:
The Bank class simulates a simple banking system with the following operations:

Create a pin.

Deposit and withdraw cash.

Check balance.

Key Methods:
__init__(self):

Initializes the pin and balance attributes.

Calls the menu() method to display options for the user.

menu(self):

Displays a menu with options to create a pin, deposit, withdraw, check balance, or exit.

Loops continuously, allowing the user to choose different operations.

create_pin(self):

Prompts the user to create a pin.

deposit(self):

Prompts the user to enter their pin and then deposit cash if the pin is valid.

Updates the balance.

withdraw(self):

Prompts the user to enter their pin and withdraw cash if the pin is valid and there is sufficient balance.

check_balance(self):

Prompts the user to enter their pin and displays the balance if the pin is correct.
