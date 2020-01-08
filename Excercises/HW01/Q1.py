########################################################
# Author: David Jarufe                              
# Date: Feb. 22 / 2019
#
# This program calculates the amount of ingredients
# (in Cups) needed to cook a quantity of cookies 
########################################################

SUGAR = 1.5     #Sugar needed for 48 cookies (in Cups)
BUTTER = 1      #Butter needed for 48 cookies (in Cups)
FLOUR = 2.75    #Flour needed for 48 cookies (in Cups)

#Asks user and accepts their input of cookies
cookies = int(input("How many cookies would you like to make --> "))

cookies /= 48   #Divide by 48 to find the ratio of ingredients

#Calculation for final ingredients needed for number of cookies
finSugar = SUGAR * cookies
finButter = BUTTER * cookies
finFlour = FLOUR * cookies

#Output that the user views
print("\nHere are the ingredients you need (in Cups)")
print("Sugar =", format(finSugar,".2f"))
print("Butter =", format(finButter,".2f"))
print("Flour =", format(finFlour,".2f"))
