class Hello:
    def print_pattern(self, n):
        counter = 0
        result = ""  # Store the pattern here

        for i in range(1, n + 1):
            for j in range(i):
                if counter % 2 == 0:
                    char = chr(65 + counter)  # Uppercase letter
                else:
                    char = chr(97 + counter)  # Lowercase letter
                result += char  # Append character to result
                counter += 1  # Increment counter after adding char
            result += "\n"  # Add newline after each row

        return result  # Return the entire pattern as a string


n = int(input("Enter the number: "))
a = Hello()
pattern = a.print_pattern(n)
print(pattern)
