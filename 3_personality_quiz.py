name = input("Hi! What's your name? ")
print ("Hello, "+name,"!")
age = input("How old are you? ")
print("\nYou're "+age,"""! That's awesome! Are you ready to get started? Let's find out whether you have more
introverted or extroverted tendencies!""")
total = 0

q1 = str.lower(input("Do you hate to go to big parties? Y or N "))
if (q1 == "y"):
    total = total+1
else:
    total = total

q2 = str.lower(input("\nDo you prefer to sing alone? Y or N "))
if (q2 == "y"):
    total = total+1
else:
    total = total

q3 = str.lower(input("\nDo you enjoy long hikes in nature? Y or N "))
if (q3 == "y"):
    total = total+1
else:
    total = total

q4 = str.lower(input("\nDo you like long bubble baths? Y or N "))
if (q4 == "y"):
    total = total+1

q5 = str.lower(input("\nDo you prefer to sleep alone? Y or N "))
if (q5 == "y"):
    total = total+1
else:
    total = total

q6 = str.lower(input("\nDo you prefer cats over dogs? Y or N "))
if (q6 == "y"):
    total = total+1
else:
    total = total


if (total > 3):
    total = str (total)
    print("\nYou have a score of "+total+"! We think you exhibit more introvert tendencies!")
elif (total == 3):
    total = str (total)
    print("\nYou have a score of "+total+"! We think you have both introvert and extrovert tendencies!")
elif (total < 3):
    total = str (total)
    print("\nYou have a score of "+total+"! We think you exhibit more extrovert tendencies!")
