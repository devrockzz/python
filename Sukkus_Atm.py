print('Welcome to Xyz Bank ATM') #1
restart = ('Y') #2
chance = 3 #3
balance = 2000 #4
while chance >=0: #5
    pin = int(input('Please Enter your 4 digit pin:')) #6
    if pin == (1234): #7
        print('You have entered your pin correctly:\n') #8
        while restart not in ('n','No','no','N'): #9
            print('Please press 1 For Your Balance:\n') #10
            print('Please press 2 To Make a WithDrawl:\n') #11
            print('Please press 3 To Pay in \n') #12
            print('Please press 4 To Return Card\n') #13
            option = int(input('What would you like to choose?')) #14
            if option == 1: #15
                print('your balance is Rs:',balance,'\n') #16
                restart = input('Would you like to go back?') #17 
                if restart in  ('n','No','no','N'): #18
                    print('Thank you!') #19
                    break #20
            elif option == 2: #21
                option2 = ('Y') #22
                withdrawl = float(input('How Much you world like to WidthDraw?')) #23
                if withdrawl in  [10,20,30,40,50,100]: #24
                    balance = balance - withdrawl #25
                    print('\n your balance is now: ',balance) #26
                    restart = input('Would you like to go back?') #27
                    if restart in  ('n','No','no','N'): #28
                        print('Thank you!') #29
                        break #30
                elif withdrawl!=[10,20,30,40,50,100]: #31
                    print('Invalid Amount, please Re-try\n') #32
                    restart = ('Y') #33
                elif withdrawl == 1: #34
                    withdrawl = float(input('Please Enter Desired Amount:')) #35
            elif option == 3: #36
                Pay_in = float(input('How much would you like ton pay In ?:')) #37
                balance = balance + Pay_in #38
                print(balance) #39
                restart = input('Would you like to go back?') #40
                if restart in  ('n','No','no','N'): #42
                    print('Thank you!') #43
            elif option == 4: #44
                print('Please wait while you card is returned \n') #45
                print('Thank you!') #46
                break #47
            else: #48
                print('Please enter a correct number\n') #49
                restart = ('Y') #50
                break
               
    elif pin!=('1234'): #51
        print('Incorrect Password') #52
        chance = chance - 1 #53
        if chance == 0: #54
             print('Incorrect Password') #55
             break #56
