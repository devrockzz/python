print("\n Welcome to Wasp Bank ATM")

RESTART = 'Y'

CHANCE = 3

BALANCE = 5000

while CHANCE >= 0:

  print(" \n You have " , CHANCE , " chances ")

  PIN = int(input("\n Please enter your 4 digit PIN: "))

  if PIN == 1234:

    print("\n You have entered the pin correctly !")

    while RESTART not in ('n' , 'N' , 'no' , 'No'):

      print("\n Press 1 for your Balance \n")

      print(" Press 2 to make a Withdrawl \n")

      print(" Press 3 to make a Deposit \n")

      print(" Press 4 to Return Card \n")

      OPTION = int(input("What would you like to choose? "))

      if OPTION == 1:

        print("\n Your balance is Rs: \n" , BALANCE )

        RESTART = input("\n Would you like to go back? ")

        if RESTART in ('Y'):

            break

      elif OPTION == 2:              

        WITHDRAWL = float(input("\n How Much you would like to Withdrawl? \n "))

        if (BALANCE - WITHDRAWL  >= 1000 and WITHDRAWL < BALANCE ):

          BALANCE = BALANCE - WITHDRAWL

          print('\n Your balance is now: ', BALANCE)

        else:

          print("\n Insufficient Balance \n")
        
        break

      elif OPTION == 3:

        DEPOSIT_MONEY = int(input("\n Enter the amount for deposit: "))

        if(DEPOSIT_MONEY > 0):

          BALANCE = BALANCE + DEPOSIT_MONEY

          print('\n Your balance is now: ', BALANCE)

        else:

          print("Enter valid amount \n")

        RESTART = input("\n Would you like to go back? ")

        if RESTART in ('Y'):

            break
        
      elif OPTION == 4:

          print("\n Please wait...Collect your card \n")

          print("Thank You! Have a nice day")

          break
        

      else:

        print("Please enter a correct option \n")

  else:

    print("Incorrect Password")

    CHANCE = CHANCE - 1

    if CHANCE == 0:

        print("You have no chance")

        break
