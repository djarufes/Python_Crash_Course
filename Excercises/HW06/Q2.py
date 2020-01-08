########################################################
# Author: David Jarufe
# Date: April. 10 / 2019
# This program creates a Dicitonary out of a list of
# teams that won the World Series between 1903 and 2009.
# It also lets the user choose a year between that range
# to know which team won that year and how m any times
# did they win in total between 1993 - 2009
########################################################

def main():

  #Open a file for reading
  outfile = open("WorldSeriesWinners.txt","r")

  #Read the first line from the file
  team = outfile.readline()
  
  #Turns the txt file into a list
  seriesWinners = []
  while team !="":
    winner = str(team)
    seriesWinners.append(winner)

    #Read the next line
    team = outfile.readline()

  #Call function that turns list to dictionary
  winnerDictionary = turnToDic(seriesWinners)
  
  #Call function that outputs the final output
  promptUsr(winnerDictionary,seriesWinners)
  
  #Close the file
  outfile.close()
  
def turnToDic(seriesWinners):
  
  #Find team names that only appear once
  uniqueSet = set(seriesWinners)
  uniqueList = list(uniqueSet)
  
  #Loop that finds the number of times each team has won
  n = 0             #Counter for the loop
  winList = []      #List that will be filles with winnings
  
  while n < len(uniqueList):
    wins = seriesWinners.count(uniqueList[n])
    winList.append(wins)
    n += 1
  
  #Turns two lists (key and value) into a dictionary
  finalDictionary = dict(zip(uniqueList,winList))

  return(finalDictionary)

def promptUsr(dic,series):
    
  #Accepts the user's input
  print("World Series' Winning Teams 1903 - 2009")
  year = int(input("Enter a year between 1903 - 2009 to display the winning team --> "))

  #Depends on the year, a different output will be displayed
  #to account for the 2 years were no World Series was played
  if ((year == 1904) | (year == 1994)):
    print("\nWorld Series was not played in this year")
  elif ((year > 1904) & (year < 1994)):
    loc = year - 1903 - 1
    print("\nIn ", year, ", the ",series[loc], "won the World Series!", sep="")
    print("\nBetween 1903 - 2009, the amount of times they won was --> ", dic.get(series[loc],"Entry not found"), sep="")
  elif (year > 1994):
    loc = year - 1903 - 2
    print("\nIn ", year, ", the ",series[loc], "won the World Series!", sep="") 
    print("\nBetween 1903 - 2009, the amount of times they won was --> ", dic.get(series[loc],"Entry not found"), sep="")
  else:
    loc = year - 1903
    print("\nIn ", year, ", the ",series[loc], "won the World Series!", sep="") 
    print("\nBetween 1903 - 2009, the amount of times they won was --> ", dic.get(series[loc],"Entry not found"), sep="")
    
#Call the main function
main()