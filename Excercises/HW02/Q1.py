########################################################
# Author: David Jarufe                              
# Date: Mar. 2 / 2019
#
# This program determines if the month of February
# has 28 or 29 days depending of the year (leap year
# or not)
########################################################

#Asks user to enter the year
year = int(input("Please enter a year --> "))

#Determines if the year is a leap year 
if((year % 100) == 0):      #If the year is divisibe by 100
  if ((year % 400) == 0):   #If the year is divisibe by 400
    days = 29
elif((year % 4) == 0):      #If the year is divisibe by 4
  days = 29
else:
  days = 28

#Outputs the number of days February has
if (year <= 2018):
  print("\nIn the year ",format(year,".0f"),", February had ", format(days,".0f")," days!", sep="")
else:
  print("\nIn the year ",format(year,".0f"),", February will have ", format(days,".0f")," days!", sep="")
