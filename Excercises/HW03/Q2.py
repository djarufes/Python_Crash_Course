########################################################
# Author: David Jarufe
# Date: Mar. 14 / 2019
# This program collects data and calculates the
# average rainfall over a period of years
########################################################

countY = 1          #Count needed to track years
countM = 0          #Count needed to track months
rainFallArr = []    #List of rain fall inputs
totRainFall = 0     #Initialize total rainfall

monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July',   #Month names
  'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

#Asks user to enter number of years
userInput = int(input("Please enter the number of years to collect average rainfall data --> "))

#Nested loop that iterates through the months of each year
for years in range(1,(userInput + 1),1):
    print("\nYear ",format(countY,".0f"),sep="")
    countY = countY + 1
    countM = 0
    for months in range(1,13,1):
        print("Inches of rain for the month of ",monthNames[countM],sep="")
        countM = countM + 1
        
        #Asks user for rainfall input
        rainFall = float(input("--> "))
        totRainFall += rainFall
        rainFallArr.append(rainFall)

countY = 1      #Reset month counter
countM = 0      #Reset month counter
count = 0       #Counter for use with array when printing output

#Prints output
print("\nAverage Rainfall Over A ", format(userInput,".0f"), "-Year Period", sep="")
for years in range(1,(userInput + 1),1):
    print("=====================================")
    print("\tYear ",format(countY,".0f"),sep="")
    print("=====================================")
    print("MONTH\t\tAVERAGE RAINFALL (INCHES)\n")
    countY = countY + 1
    countM = 0
    for months in range(1,13,1):
        print(monthNames[countM],"\t\t",rainFallArr[count], sep="")
        countM = countM + 1
        count = count + 1
        
totMonths = userInput * 12  #Calculates total months
avgRainFall = totRainFall / totMonths   #Calculates average rainfall
print("\nTotal Number of Months: ",format(totMonths,".0f"),sep="")
print("Total Inches of Rainfall: ",format(totRainFall,".0f"),sep="")
print("Average Rainfall Per Month for Entire Period: ",format(avgRainFall,".0f")," in.", sep="")





