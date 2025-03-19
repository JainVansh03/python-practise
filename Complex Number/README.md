**Complex Number
**


Purpose:
The ComplexNumber class allows for the creation of complex numbers and supports various operations (addition, subtraction, multiplication, division, conjugation, equality check) using Python's special (dunder) methods.

Key Methods:
__init__(self, real, img):

Initializes a complex number with real and imaginary parts.

__str__(self):

Defines the string representation of a complex number. If the real part is 0, it only shows the imaginary part, and it formats the number correctly based on whether the imaginary part is positive or negative.

__add__(self, other):

Adds two complex numbers by adding their real and imaginary parts separately.

__sub__(self, other):

Subtracts one complex number from another by subtracting their real and imaginary parts.

__mul__(self, other):

Multiplies two complex numbers using the standard formula for complex multiplication.

__truediv__(self, other):

Divides one complex number by another, using the formula for complex division (raises an error if division by zero occurs).

conjugate(self):

Returns the conjugate of the complex number (changes the sign of the imaginary part).

__eq__(self, other):

Checks if two complex numbers are equal by comparing their real and imaginary parts.

menu(self, complex_numbers):

Provides a menu of operations for the user, including:

Adding, subtracting, multiplying, and dividing complex numbers.

Printing the conjugate of a complex number.

Checking if complex numbers are equal.

Printing all complex numbers.

Exiting the program.

Supports multiple complex numbers in the list and performs the selected operation using dunder methods.

Driver Code:
The program prompts the user to enter a number n representing how many complex numbers they want to create.

The program then asks for the real and imaginary parts of each complex number and stores them in a list.

After displaying all entered complex numbers, the menu() function is called to allow the user to perform various operations on those complex numbers.
