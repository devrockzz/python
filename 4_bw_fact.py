# factorial for a number
def factorial(n):
    return 1 if n ==0 or n ==1 else n * factorial(n-1) #n! = n* (n-1)* (n-2)*...*1
n = 6
print("The factorial for, ", n, "is:", factorial(n))