
print("\nWelcome to XYZ Bank ATM\n")

chance = 3

restart = 'Y'

balance = 5000

while chance >= 0:

  if restart in "noNoNO":

    print("\nThank you! Have a nice day.\n")

    break

  print("You have" , chance , "chances\n")

  pin = int(input("Please enter your 4 digit pin: "))

  if pin == 1234:

    print("\nYou have entered pin correctly\n")

    while restart not in "noNoNO":

      print('\nPlease press 1 for cheack balance\n')

      print('\nPlease press 2 to make a withdrawl\n')

      print('\nPlease press 3 to a deposit\n')

      print('\nPlease press 4 to return card\n')

      option = int(input('\nWhat would you like to choose: '))

      # Cheack Balance 

      if option == 1:

        print('\nYour balance is Rs: ' , balance  )

        restart = input('\nWould you like to go back: ')

        if restart in "yesYESYes":

            continue
 
      # Withdrawl Money 

      elif option == 2:

        withdrawl_amount = int(input("\nPlease enter amount for withdrawl: "))

        if(balance - withdrawl_amount >= 1000 and withdrawl_amount < balance):

          balance = balance - withdrawl_amount

          print('\nYour balance' , balance)

        else:

          print("\nInsufficient balance\n")

        restart = input("\nWould you like to go back: ")

        if restart in "yesYESYes":

          continue

      #  Deposit Money  

      elif option == 3:

        deposit_money = int(input("\nEnter the amount for deposit: "))

        if(deposit_money > 0):

          balance = balance + deposit_money

          print("\nBalance is Rs.: " , balance)

        else:

          print("\nEnter valid amount\n")

        restart = input('\nWould you like to go back: ')  

        if restart in "yesYESYes":

           continue

      #  Collect Card    

      elif option == 4:

        print("\nPlease wait...Collect your card")

        restart = 'no'

        break
   
      else:

        print("\nPlease enter a correct option\n")

  else:

    print("\nIncorrect password\n")

    chance = chance - 1

    if chance == 0:

      break


            

            

        

            

            
