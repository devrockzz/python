print("Welcome to Felicitous Bank ATM.")  #pleasing and fortunate
balance = 5000
chance = 2
restart ="Y"
while chance >=0:
    pin = int(input("Please enter 4-digit PIN: "))
    if pin ==(3971):
        print("Fuiiyoo...You have entered the correct PIN!\n")
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
                withdrawl = int(input("How much money you want to withdraw??"))
                if withdrawl in [10,20,50,100,500,100]:
                    balance = balance - withdrawl
                    print("Niece/Nephew, You have only: ", balance,"left with you!\n")
                    break
            elif option == 3:
                pay_in = int(input("How much money you want to enroll:"))
                balance = balance + pay_in
                print("Fuiyyoo...Your balance is: ", balance, "\n")
                break
            elif option == 4:
                print("Please collect your card")
                print("Thank you. Have a nice day!\n")
                break
            else:
                print("Welcome to Felicitous Bank ATM. How may I help you?\n")
    elif pin != (3971):
        print("Incorrect password")
        chance = chance - 1
        if chance == 0:
            print("Hiyaa...Incorrect password!")            
            