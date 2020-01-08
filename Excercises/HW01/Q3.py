##########################################################
# Author: David Jarufe                              
# Date: Feb. 22 / 2019
#
# This program calculates the the amount of money that
# will be in an account after a specified number of
# years, given the beginning amount of money, account's
# interest rate, compoundedness, and number of years the
# account is left untouched. 
##########################################################

#Asks user to input measurements
print("To calculate the amount of money that will be in your account after the specified number of years:")
startQuant = float(input("Enter the amount of principal originally deposited into your account ($) --> "))     #Starting amount of money
intRate = float(input("Enter the annual interest rate paid by your account (%) --> "))      #Account's Interest rate
intRateComp = float(input("Enter the number of times per year that the interest is compounded (monthly, quarterly, etc.) --> "))      #Interest rate compoundedness
earnYears = float(input("Enter number of years the account will be left to earn interest --> "))      #Number of years the account is left

#Calculations for the the amount of money that will be in an account
intRate /= 100      #Divide by 100 to move the decimal point to the current position. 
finalQuant = startQuant * ((1 + (intRate / intRateComp)) ** (intRate * earnYears))

#Output that the user views
print("\n","You will have $",format(finalQuant,",.2f")," after ",format(earnYears,".0f")," years.", sep="")
