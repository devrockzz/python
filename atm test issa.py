print("Welcome to Wayne Bank ATM.")  
balance = 50000
chance = 2
restart ="Y", "y"
while chance >=0:
    pin = int(input("Please enter 4-digit PIN: "))
    if pin ==(1111):
        print("yippee...You have entered the correct PIN!\n")
        while restart not in ('N','n','NO','no','No'):
            print("Press 1 for Checking Balance")
            print("Press 2 for Withdrawl")
            print("Press 3 for Pay-in cash")
            print("Press 4 for Card return\n")
            option = int(input("Please select an option: "))
            if option == 1:
                print("Niece/Nphew, Your balance is: ", balance,"\n")
                break
            elif option == 2:
                withdrawal = int(input("How much money you want to withdraw??"))
                while withdrawal <= balance:
                    balance = balance - withdrawal
                    print("woohoo, You have only: ", balance,"left with you!\n")
                    break
            elif option == 3:
                pay_in = int(input("How much money you want to enroll:"))
                balance = balance + pay_in
                print("woohoo...Your balance is: ", balance, "\n")
                break
            elif option == 4:
                print("Please collect your card")
                print("Thank you. Have a nice day!\n")
                break
            else:
                print("Welcome to Wayne Bank ATM. How may I help you?\n")
    elif pin != (1111):
        print("Incorrect password")
        chance = chance - 1
        if chance == 0:
            print("oopsie... Incorrect password!")            
            