number=[] 
for x in range(2000, 3201): 
    if (x%7==0) and (x%5>0): 
        number.append(str(x)) 
        print (','.join(number))