########################################################
# Author: David Jarufe
# Date: April. 04 / 2019
# This program reads the random numbers from a file
# and prints the quantity and their sum
########################################################

def main():
  #Open a file for writing
  outfile = open("randNums.txt","r")

  #Reads the first line from the file 
  rNum = outfile.readline()
  totNums = 0   #Variable declaration for future use in addition
  count = 0     #Variable declaration for future use counting

  print("All the numbers in the randNums.txt file are:\n")
  
  #Loop that prints the numbers
  while (rNum != ""):
    numInFile = float(rNum)

    #Print the number in that line
    print(format(numInFile,".0f"))
    totNums += numInFile
    count += 1

    #Read the next line in the file
    rNum = outfile.readline()

  #Print the final output that the user sees
  print("\nThere were ",count," numbers in the file",sep="")
  print("The total of all these numbers is -> ",format(totNums,".0f"), sep="")

  #Close the file
  outfile.close()

#Call the main function
main()
  
