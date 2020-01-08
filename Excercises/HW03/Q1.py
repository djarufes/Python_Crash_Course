########################################################
# Author: David Jarufe
# Date: Mar. 14 / 2019
# This program finds the sum and average
# of multiple numbers inputted by user
# until a negative number stops the loop
########################################################

numSum = 0  #Sum of all numbers inputted
count = 0   #Keeps count of number inputted

#Asks user to enter numbers
number = int(input("Please enter a positive number OR negative number when done --> "))

#Repeats until a negative number is inputted
while(number >= 0):
    count = count + 1
    numSum += number
    number = int(input("Please enter a positive number OR negative number when done --> "))

#Output the user views
if (count == 0):
    print("\nNo calculations were able to be made :(" , sep="")
else:
    numAvg = numSum / count     #Calculate avg
    print("\nThe sum of all inputted numbers is: ",format(numSum,".0f"),sep="")
    print("The average of all inputted numbers is: ",format(numAvg,".2f"),sep="")
