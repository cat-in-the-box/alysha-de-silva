#Tip Calculator for Living wage in Massachusettes as of 2019
#Three versions will be made:
# version 1: Average minimum wage (service affects whether the tip lands below or above)
# version 2: Bringing the tip up to minimum wage, with extra good service on top
# version 3: Bring tip up to living wage, and extra service goes on top
#Assumption: coffee shop that srvices 20 people/hr with 3 employees and an average bill of $5

#Minimum Tip Wage in MA as of Jan 1, 2019 is $4.35 / hr
#Living wage in MA as of Jan 1, 2019 ia $13.96 / hr

tip_wage = float(4.35)
living_wage = float(13.96)

choice = input("Would you like version 1, version 2 or version 3? ")

if choice == "1":
    bill = float(input("How much is your bill?: "))
    percent = float (input("What percentage would you like to tip?: "))
    tip = round (float( (percent / 100) * bill) , 2)
    pay = round (float(bill + tip), 2)
    #Version 1: Average minimum wage (service affects whether the tip lands below or above)
    while tip < tip_wage: #While means that the prompt will continue until this is not true, or until the code ends.
        less = str.lower(input("\nYour tip of $"+str(tip)+" is less than the minimum wage for your server. \nWould you consider tipping more?"))
        if less == "no": #If the user doesn't want to consider a higher tip, the total will show
            print("\nThat's okay, you should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
             ".\nYou should leave a total of $" +str(pay)+ ".")
            quit()
        else: # If the user is open to reconsidering the tip, a new percentage will be prompted and calculated.
            percent = float (input("\nWhat percentage would you like to tip?: "))
            tip = round (float( (percent / 100) * bill) , 2)
            pay = round (float(bill + tip), 2)
            print("\nYou should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
             ".\nYou should leave a total of $" +str(pay)+ ". Thank you for reconsidering!")
    else: #if the tip given is greater than the minimum tip wage, it will be calcualted and displayed.
         print("\nYou should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
        ".\nYou should leave a total of $" +str(pay)+ ".")

elif choice == "2":
    bill = float(input("How much is your bill?: "))
    percent = float (input("What percentage would you like to tip?: "))
    tip = round (float( (percent / 100) * bill) , 2)
    pay = round (float(bill + tip), 2)
    #Version 2: Bringing the tip up to minimum wage, with extra good service on top
    while tip < tip_wage:
         less = str.lower(input("\nYour tip of $"+str(tip)+" is less than the minimum wage for your server. \nWould you consider increasing your tip to match the minimum wage of $"+str(tip_wage)))
         if less == "no":
            print("\nThat's okay, you should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
             ".\nYou should leave a total of $" +str(pay)+ ".")
            quit()
         else:
            tip = tip_wage# If the user is open to reconsidering the tip, a new percentage will be prompted and calculated.
            pay = round (float(bill + tip), 2)
            print("\nYou should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
             ".\nYou should leave a total of $" +str(pay)+ ". Thank you for reconsidering!")
            while tip == tip_wage:
                more = str.lower(input("\nIf you consider your service to be exceptional today, would you consider adding on an additional tip? "))
                if more == "no": #If the customer only wants to tip the minimum tipping wage
                    print("\nNo problem! Thank you for your initial tip and have a great day!")
                    quit()
                else: #if the customer had great service and would like to tip more
                    percent = float (input("What percentage would you like to tip?: "))
                    tip = round (float( (percent / 100) * bill) , 2)
                    pay = round (float(bill + tip + tip_wage), 2)
                    print("\nThank you again! Your total would now be $"+ str(pay),". Have a great day!")
                    quit()
    else:
         print("\nYou should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
        ".\nYou should leave a total of $" +str(pay)+ ".")  

elif choice == "3":
    bill = float(input("How much is your bill?: "))
    percent = float (input("What percentage would you like to tip?: "))
    tip = round (float( (percent / 100) * bill) , 2)
    pay = round (float(bill + tip), 2)
    #Version 3: Bring tip up to living wage, and extra service goes on top
    while tip < living_wage:
         less = str.lower(input("\nYour tip of $"+str(tip)+" is less than the living wage for your server. Would you consider increasing your tip to match the living wage of $"+str(living_wage)))
         if less == "no": 
            print("\nThat's okay, you should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
             ".\nYou should leave a total of $" +str(pay)+ ".")
            quit()
         else:# If the user is open to reconsidering the tip, a new percentage will be prompted and calculated.
            tip = living_wage
            pay = round (float(bill + tip), 2)
            print("\nYou should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
             ".\nYou should leave a total of $" +str(pay)+ ". Thank you for reconsidering!")
            while tip == living_wage:
                more = str.lower(input("\nIf you consider your service to be exceptional today, would you consider adding on an additional tip? "))
                if more == "no": #If the customer only wants to tip the minimum tipping wage
                    print("\nNo problem! Thank you for your initial tip and have a great day!")
                    quit()
                else: #if the customer had great service and would like to tip more
                    percent = float (input("What percentage would you like to tip?: "))
                    tip = round (float( (percent / 100) * bill) , 2)
                    pay = round (float(bill + tip + living_wage), 2)
                    print("\nThank you again! Your total would now be $"+str(pay),". Have a great day!")
                    quit()
    else:
         print("\nYou should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+
        ".\nYou should leave a total of $" +str(pay)+ ".")

else:
    print("\nPlease select one of the choices: 1, 2 or 3")