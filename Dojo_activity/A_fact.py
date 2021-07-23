no = int(input("Enter the number to find factorial:"))
fact = 1
for i in range(1 ,no+1):
    fact = fact * i
print("factorial of the number", no , "is:", fact)