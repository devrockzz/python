
print("\nWelcome to XYZ Bank ATM\n")

chance = 3

restart = 'Y'

balance = 5000

while chance >= 0:

  print("You have" , chance , "chances\n")

  pin = int(input("Please enter your 4 digit pin: "))

  if pin == 1234:

    while restart not in ('n' , 'N' , 'no' , 'No'):

      print('\nPlease press 1 for cheack balance\n')

      print('Please press 2 to make a withdral\n')

      print('Please press 3 to deposit\n')

      print('Please 4 to return card\n')

      option = int(input('What would you like to choose: '))

      # Cheack Balance 

      if option == 1:

        print('Your balance is Rs: \n' , balance)

        restart = input('Would you like to go back: ')

        if restart in ('y' , 'Y' , 'yes' 'Yes'):

          break

        # Withdrawl Money 

      elif option == 2:

        withdrawl_amount = int(input("Please enter amount for withdrawl: "))

        if(balance - withdrawl_amount >= 1000 and withdrawl_amount < balance):

          balance = balance - withdrawl_amount

          print('Your balance' , balance)

        else:

          print("Insufficient balance\n")


        if restart in ('Y' 'Yes'):

            break
 
          # Deposit Money 

      elif option == 3:

        deposit_money = int(input("\nEnter the amount for deposit: "))

        if(deposit_money > 0):

          balance = balance + deposit_money

          print("Balance is: " , balance)

        else:

          print("Enter valid amount\n")

        if restart in ('Y'):

            break

      elif option == 4:

        print("\n Please wait...Collect your card \n")

        print("Thank You! Have a nice day")

        break
   

    else:

         print("Please enter a correct option\n")


  else:

    print("\nIncorrect password\n")

    chance = chance - 1

    if chance == 0:

      print("You have no more chance\n")

      break

        

        

        

            

            
