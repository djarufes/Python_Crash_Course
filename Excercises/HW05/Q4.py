########################################################
# Author: David Jarufe
# Date: April. 04 / 2019
# This program reads from a file containing midyear
# population of the US and output its average annual
# change and the greatest increase and decrease in
# population
########################################################

def main():

  #Open a file for reading
  outfile = open("USPopulation.txt","r")

  #Read the first line from the file
  numPop = outfile.readline()
  
  #Turns the txt file into a list
  USpop = []
  while numPop !="":
    yearPop = float(numPop)
    USpop.append(yearPop)

    #Read the next line
    numPop = outfile.readline()

  popCompute(USpop)     #Calls the function that computes the outputs

  #Close the file
  outfile.close()

#Function that computes the desired outputs
def popCompute(USpop):

  #Initializing variables
  size = len(USpop)
  count = 0
  avgPop = 0
  year = 1950
  highPopDif = 0
  highYear = 0
  lowPopDif = 1000000
  lowYear = 0
  
  #Loop that sums all populations to find the average
  while(count < size - 1):
    popDif = USpop[count + 1] - USpop[count]
    avgPop += popDif
    count += 1

    #Finds the year with the highest population change
    if popDif > highPopDif:
      highPopDif = popDif
      highYear = year

    #Finds the year with the lowest population change
    if popDif < lowPopDif:
      lowPopDif = popDif
      lowYear = year

    year += 1

  #Computes the average population
  avgPop /= size

  #Print output
  print("The average annual change in population during the time period is -> ",format(avgPop,".0f"),sep="")
  print("The year with the greatest increase in population during the time period -> ", format(highYear,".0f"),sep="")
  print("The year with the smallest increase in population during the time period -> ", format(lowYear,".0f"),sep="")

#Call the main function
main()
