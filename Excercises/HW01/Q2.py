##########################################################
# Author: David Jarufe                              
# Date: Feb. 22 / 2019
#
# This program calculates the number of grapevines that
# will fit in a row of a vineyard given the number of
# grapevines, the length of the row (in ft), the amount
# of space used by an end-post assembly (in ft), and the
# space between vines (in ft),
##########################################################

#Asks user to input measurements
print("To calculate the number of grapevines that will fit in a row:")
rowLen = float(input("Enter the length of the row (in feet) --> "))     #Length of the row input
spaceUsed = float(input("Enter the amount of space used by the end-post assembly (in feet) --> "))      #Space used input
spaceVines = float(input("Enter the amount of space between the vines (in feet) --> "))      #Space between the vines input

#Calculations for the number of grapevines that will fit in the row.
grapeVines = (rowLen - (2 * spaceUsed)) / spaceVines

#Output that the user views
print("\n",format(grapeVines,".0f")," grapevines will fit in the row.", sep="")

