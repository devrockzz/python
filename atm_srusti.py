print('Welcome to SBI Bank ATM')
restart = "Y"
chance = 2
balance = 35000
while chance >=0:
    pin = int(input('Please Enter your 4 digit pin:'))
    if pin == (1234):
        print('You have entered your pin correctly:\n')
        while restart not in ('n','No','no','N'):
            print('Please press 1 For Your Balance:\n')
            print('Please press 2 To Make a withdrawl:\n')
            print('Please press 3 To Pay_in \n')
            print('Please press 4 To Return Card\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
               print('your balance is Rs:',balance,'\n')
               break
            elif option == 2:
                withdrawl = float(input('How Much you would  like to withdrawl?'))
                if withdrawl in  [10,20,30,40,50,100]:
                    balance = balance - withdrawl
                    print('\n your balance is now: ',balance)
                    break
                elif withdrawl not in [10,20,30,40,50,100]:
                 print('Invalid Amount, please Re-try\n')
                 restart = "Y"
            elif option == 3:
                Pay_in = float(input('How much would you like to pay In ?:'))
                balance = balance + Pay_in
                break
            elif option == 4:
                print('Please wait while you card is returned \n')
                print('Thank you!')
                break
            else:
                print('Please entered a correct number\n')
                restart =  "Y"      
    elif pin != ('1234'):
        print('Incorrect Password')
        chance = chance - 1
        if chance == 0:
             print('Incorrect Password')
             break

