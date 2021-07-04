n = int(input()) #input() function takes input as string type
                #int() converts it to integer type
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)


#https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md
#https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
#https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md
