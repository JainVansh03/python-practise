
def print_pattern(n):
    start = 1  
    row = []
    for i in range(1, n + 1):
        row = []
        num = start
        for j in range(i):
            
            row.append(num)
            row.append("")
            num = num + (n - (j+1))
            
            
        print(*row[::-1])
        start += 1
      

n = 6
print_pattern(n)