'''Complex Number Program Using Dunder Method'''




class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.real == 0:
            s = f"({self.img}i)"
        elif self.img < 0:
            s = f"({self.real}-{abs(self.img)}i)"
        else:
            s = f"({self.real}+{self.img}i)"
        return s

    def __add__(self, other):
        realnum = self.real + other.real
        imgnum = self.img + other.img
        return ComplexNumber(realnum, imgnum)

    def __sub__(self, other):
        realnum = self.real - other.real
        imgnum = self.img - other.img
        return ComplexNumber(realnum, imgnum)

    def __mul__(self, other):
        realnum = self.real * other.real - self.img * other.img
        imgnum = self.real * other.img + other.real * self.img
        return ComplexNumber(realnum, imgnum)

    def __truediv__(self, other):
        denominator = other.real**2 + other.img**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero")
        
        realnum = (self.real * other.real + self.img * other.img) / denominator
        imgnum = (self.img * other.real - self.real * other.img) / denominator
        return ComplexNumber(realnum, imgnum)

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.img)

    def __eq__(self, other):
        return (self.real == other.real) and (self.img == other.img)

    def menu(self, complex_numbers):
        while True:
            user_input = int(input(""" 
            Hello, how would you like to proceed?
            1. To Add Complex Numbers press 1
            2. To Subtract Complex Numbers press 2
            3. To Multiply Complex Numbers press 3
            4. To Divide Complex Numbers press 4
            5. To Print Conjugate press 5
            6. To Check whether the Complex Numbers are Equal or Not press 6
            7. To Print the Complex Numbers press 7
            8. To Exit press 8
            """))

            if user_input == 1:
                # Add complex numbers using dunder method for multiple numbers
                if len(complex_numbers) > 1:
                    result = complex_numbers[0]
                    for num in complex_numbers[1:]:
                        result = result + num  # Using __add__ dunder method
                    print(f"Result of addition: {result}")
                else:
                    real = int(input("Enter real part of the second complex number: "))
                    img = int(input("Enter imaginary part of the second complex number: "))
                    result = complex_numbers[0] + ComplexNumber(real, img)
                    print(f"Result of addition: {result}")

            elif user_input == 2:
                # Subtract complex numbers using dunder method for multiple numbers
                if len(complex_numbers) > 1:
                    result = complex_numbers[0]
                    for num in complex_numbers[1:]:
                        result = result - num  # Using __sub__ dunder method
                    print(f"Result of subtraction: {result}")
                else:
                    real = int(input("Enter real part of the second complex number: "))
                    img = int(input("Enter imaginary part of the second complex number: "))
                    result = complex_numbers[0] - ComplexNumber(real, img)
                    print(f"Result of subtraction: {result}")
            
            elif user_input == 3:
                # Multiply complex numbers using dunder method for multiple numbers
                if len(complex_numbers) > 1:
                    result = complex_numbers[0]
                    for num in complex_numbers[1:]:
                        result = result * num  # Using __mul__ dunder method
                    print(f"Result of multiplication: {result}")
                else:
                    real = int(input("Enter real part of the second complex number: "))
                    img = int(input("Enter imaginary part of the second complex number: "))
                    result = complex_numbers[0] * ComplexNumber(real, img)
                    print(f"Result of multiplication: {result}")
            
            elif user_input == 4:
                # Divide complex numbers using dunder method for multiple numbers
                if len(complex_numbers) > 1:
                    try:
                        result = complex_numbers[0]
                        for num in complex_numbers[1:]:
                            result = result / num  # Using __truediv__ dunder method
                        print(f"Result of division: {result}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    real = int(input("Enter real part of the second complex number: "))
                    img = int(input("Enter imaginary part of the second complex number: "))
                    try:
                        result = complex_numbers[0] / ComplexNumber(real, img)
                        print(f"Result of division: {result}")
                    except ValueError as e:
                        print(f"Error: {e}")
            
            elif user_input == 5:
                # Print conjugates using dunder method
                print(f"Conjugate of the first complex number: {complex_numbers[0].conjugate()}")
                if len(complex_numbers) > 1:
                    for i, num in enumerate(complex_numbers[1:], 2):
                        print(f"Conjugate of complex number {i}: {num.conjugate()}")
            
            elif user_input == 6:
                # Check equality of complex numbers using __eq__ dunder method
                if len(complex_numbers) > 1:
                    print("Here is the list of complex numbers:")
                    for i, num in enumerate(complex_numbers, 1):
                        print(f"{i}. {num}")
                    
                    # Ask the user to select two complex numbers for comparison
                    first_choice = int(input(f"Select the first complex number to compare (1-{len(complex_numbers)}): ")) - 1
                    second_choice = int(input(f"Select the second complex number to compare (1-{len(complex_numbers)}): ")) - 1
                    
                    result = complex_numbers[first_choice] == complex_numbers[second_choice]
                    print(f"Result of Is Equal?: {result}")
                else:
                    real = int(input("Enter real part of the second complex number: "))
                    img = int(input("Enter imaginary part of the second complex number: "))
                    result = complex_numbers[0] == ComplexNumber(real, img)
                    print(f"Result of Is Equal?: {result}")

            elif user_input == 7:
                # Print all complex numbers
                for i, num in enumerate(complex_numbers, 1):
                    print(f"Complex Number {i}: {num}")

            elif user_input == 8:
                print("Exiting...")
                break

            else:
                print("Invalid input, try again!")


# Driver code
complex_numbers = []
n = int(input("How many complex numbers would you like to enter? "))
for i in range(n):
    a = int(input(f"Enter Real part of complex number {i+1}: "))
    b = int(input(f"Enter Imaginary part of complex number {i+1}: "))
    complex_numbers.append(ComplexNumber(a, b))

print("List of complex numbers entered:")
for num in complex_numbers:
    print(num)

complex_numbers[0].menu(complex_numbers)  # Trigger menu for multiple complex numbers
