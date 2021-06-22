n = int(input());
fact = 1
if (n == 0 or n == 1):
  print("The Factorial is", fact)
elif(n >=2):
  for i in range(2,n+1):
    fact = fact * i
  print("The factorial is", fact)
else:
  print("The value is wrong")
