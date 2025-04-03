def ft(n):
    counter = 1 
    for i in range(1,n+1):
        for j in range(i):
            print(counter, end = " ")
            counter +=1
        print("\n")
        
        
        
n= int(input("Enter the number:"))
ft(n)
