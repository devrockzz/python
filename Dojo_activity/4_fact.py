

fact = 1

n = int(input("Enter a number : "))

if n < 0:

    print("Plz.. enter a valid integer value")

else:

    for i in range(1 , n+1):

        fact = fact * i

    print("Factorial of " , n , " is : " , fact)     

 

    