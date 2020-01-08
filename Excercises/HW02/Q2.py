########################################################
# Author: David Jarufe                              
# Date: Mar. 2 / 2019
#
# This program determines what discount will a
# buyer receive depending on how many packages he/she
# purchases
########################################################

RETAIL = 99     #Price per package ($)

#Asks user to enter the quantity of packages ordered
packages = int(input("Please enter the number of packages being ordered --> "))

#Determines what discount will the buyer receive
if((packages >= 10) and (packages <= 19)):      #If quantity is between 10 - 19
    discount = 10
elif((packages >= 20) and (packages <= 49)):    #If quantity is between 20 - 49
    discount = 25
elif((packages >= 50) and (packages <= 99)):    #If quantity is between 50 - 99
    discount = 35    
elif(packages >= 100):                          #If quantity is greater than 100
    discount = 45  
else:
    discount = 0

#Calculates the total amount 
totAmount = RETAIL * packages       #Total price without discount
if(packages >= 10):
    totAmount -= totAmount * (discount / 100)   #Add the discount to calculated amount

#Outputs the final discount and total purchase amount
print("\nReceived discount: ",format(discount,".0f"),"%", sep="")
print("Total amount of the purchase after the discount: $",format(totAmount,",.2f"),sep="")
