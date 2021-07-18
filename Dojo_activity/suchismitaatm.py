print('Welcome to Xyz Bank ATM')
restart = 'Y'
chance = 3
balance = 2000
pin = 1234
while chance != 0:
    pin = int(input('Please Enter your 4 digit pin : '))
    if pin != 1234:
        chance=chance-1
        print("wrong pin,you have", chance,"chance left")
    else:
        print('You have entered your pin correctly:\n')
        print('Please press 1 For Your Balance:\n')
        print('Please press 2 To Make a Withdrawl:\n')
        print('Please press 3 To Pay in \n')
        print('Please press 4 To Return Card\n')
        option = int(input('What would you like to choose: '))
    if option == 1:
            print('your current balance is Rs: \n',balance)
            restart = input('Would you like to go back: \n')
            if restart in ("y"):
                 break
            
    elif option == 2:
        withdrawl = int(input('How Much would u like to Withdrawl?'))
        if(withdrawl<balance):
            balance = balance - withdrawl
            print('\n your balance is now: ',balance)
        else:
            print('insufficient balance\n')
            break
    elif option == 3:
                Pay_in = int(input('How much would you like ton pay In ?:'))
                balance = balance + Pay_in
                print("current balance is:\n",balance)
                break
    elif option == 4:
                print('Please wait while you card is returned \n')
                print('Thank you!')
                break
            


