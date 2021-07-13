print("Welcome to Felicitous Bank-ATM\n") #pleasing and fortunate
balance = 5000
restart = 'Y' #how do i know that i have to define this variable?
chance = 2 #chance just for a better container name
while chance >= 0: #a while loop is used when a section of code is repeated for unknown number of times until a specific condition is met
    pin = int(input("Please enter the 4 digit PIN:"))
    if pin == (3971):
        print("Fuiiyoo...You have entered the PIN correctly.\n")
        while restart not in ('N', 'n', 'no', 'NO'):  ##why this condition? for isnt used cause we do not know how long we want to play with this XD!
            print("Press option 1 for Check Balance.")
            print("Press option 2 for Withdrawl.")
            print("Press option 3 for Pay-in.")
            print("Press option 4 for Return Card.\n")
            option = int(input('Please choose an option: '))
            if option == 1:
                print("Fuiyoo!!!...Your balance is:", balance)
                print("Thank you. Have a nice day!\n")  #\n gives a space between two lines.
                break
            elif option == 2:
                withdrawl = int(input("How much would you like to withdrawl: "))
                if withdrawl in [10,20,30,50,100,500,1000]:
                    balance = balance - withdrawl
                    print("Nephew/Niece, look! now you have only: ", balance, "\n")
                    if restart in ('N', 'n', "NO", "no","No"):
                        print("Thank You!")
                        print("Bbye...Have a nice day!\n")
                        break
            elif option == 3:
                 pay_in = float(input("What amount do you want to roll:"))
                 balance = balance + pay_in
                 print("Fuiyoo...the balance increased to:", balance,"\n")
                 break
            elif option == 4:
                print("Thank you for using Felicitous Bank-ATM")
                print("Have a nice day!\n")
                break
            elif option not in [1, 2, 3, 4]:
                print("Welcome to Felicitous Bank-ATM, How can i help you?\n")
                break         
    elif pin != (3971):
        print("Incorrect password")
        chance =chance - 1
        if chance == 0:
            print("Hiyaa...Incorrect password!")
            break


        
