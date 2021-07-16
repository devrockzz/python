print('Welcome to Wayne Bank ATM')
restart = "Y", "y"
chance = 2
balance = 50000
while chance >=0:
    pin = int(input('Please Enter your 4 digit pin:'))
    if pin == (1111):
        print('yippee...You have entered your pin correctly:\n')
        while restart not in ('n','No','no','N'):
            print('Please press 1 For Your Balance:\n')
            print('Please press 2 To Make a WithDrawal:\n')
            print('Please press 3 To Pay_in \n')
            print('Please press 4 To Return Card\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
               print('your balance is Rs:',balance,'\n')
               break
            elif option == 2:
                withdrawal = int(input("How much money you want to withdraw??"))
                while withdrawal <= balance:
                    balance = balance - withdrawal
                    print("woohoo, You have only: ", balance,"left with you!\n")
                    break
            elif option == 3:
                Pay_in = float(input('How much would you like to pay In ?:'))
                balance = balance + Pay_in
                print("your updated balance is", balance)
                break #the error in option 3 was there was no _ in the declaration part.
            elif option == 4:
                print('Please wait while you card is returned \n')
                print('Thank you!')
                break
    elif pin != ('1111'):
        print('Incorrect Password')
        chance = chance - 1
        if chance == 0:
             print('Incorrect Password')
             break
