bill = float(input("How much is your bill?: "))
percent = float (input("What percentage would you like to tip?: "))
tip = round (float( (percent / 100) * bill) , 2)
pay = round (float(bill + tip), 2)

print("You should pay a tip of $"+ str(tip), "for your bill of $"+ str(bill)+ ". \nYou should leave a total of $" +str(pay)+ ".")