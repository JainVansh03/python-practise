class Hello:
    def print_pattern(self, n):
        counter = 0

        for i in range(1, n + 1):
            for j in range(i):
                if counter % 2 == 0:
                    char = chr(65 + counter)  # Uppercase
                else:
                    char = chr(97 + counter)  # Lowercase
                print(char, end="")  # Print without newline
                counter += 1  # Increment counter after printing
            print()  # Newline after each row


n = int(input("Enter the number: "))
a = Hello()
a.print_pattern(n)
