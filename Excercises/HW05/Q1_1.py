########################################################
# Author: David Jarufe
# Date: April. 04 / 2019
# This program writes a series of random numbers to a
# file depending on how many the user wants
########################################################

import random

def main():
  #Open a file for writing
  outfile = open("randNums.txt","w")

  #Get the input from the user
  userInput = int(input("Please enter how many random numbers you want to generate --> "))

  #Loop that generates the random numbers
  count = 0
  while (count < userInput):
    rNum = random.randint(1,500)
    outfile.write(str(rNum) + '\n')
    count = count + 1

  #Close the file
  outfile.close()
  print("Random numbers were written to randNums.txt")

#Call the main function
main()
  
