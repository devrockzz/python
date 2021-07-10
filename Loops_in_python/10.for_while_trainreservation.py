travelling = input("yes or no:")#yes

while travelling == 'yes':

    num = int(input("number of people travelling:"))#2

    for num in range(1, num + 1):#num = num +1 # range 0 -1 , 0+1=1->to enter the info, 1+1=2->enter the info
        name = input("Name:")
        age = input("Age:")
        sex = input("Male or Female:")

        print(name)
        print(age)
        print(sex)

    travelling = input("Oops! forgot someone:")