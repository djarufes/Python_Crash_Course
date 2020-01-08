########################################################
# Author: David Jarufe
# Date: Mar. 14 / 2019
# This program predicts the approximate size of a
# population of organisms after a given period of time
########################################################

#Starting values that the user inputs
startingNum = int(input("Starting number of organisms --> "))
avgInc = int(input("Average daily increase (in %) --> "))
dayNum = int(input("Number of days to multiply --> "))

count = 1   #Tracks number of days

#Print output
print("\nApproximate Size of a Population of Organisms")
print("=============================================")
print("DAY APPROXIMATE\t\t POPULATION\n")
print(count,"\t\t\t",format(startingNum,".3f"))

while(count < dayNum):
    count = count + 1
    startingNum += (startingNum * (avgInc / 100))
    print(count,"\t\t\t",format(startingNum,".3f"))
