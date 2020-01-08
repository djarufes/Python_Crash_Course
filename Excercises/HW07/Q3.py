########################################################
# Author: David Jarufe
# Date: April. 18 / 2019
# This program does different functions with a file that
# cointains 654 sets of winning numbers from the 
# Pwerball Lottery.
########################################################

def main():

  #Open a file for reading
  outfile = open("pbnumbers.txt","r")

  #Read the first line from the file
  nextLine = outfile.readline()
  
  #Turns the txt file into a list
  lotteryNums = []
  while nextLine !="":
    lineRead = str(nextLine)
    lotteryNums.append(lineRead)

    #Read the next line
    nextLine = outfile.readline()
    
  #Split lotteryNums into an list of the 5 numbers and a list of Powerball numbers
  count = 0
  fiveNums = []
  pBallNums = []
  totalNums = []
  while(count < len(lotteryNums)):      #Separate each index of lotteryNums list
    count2 = 0                          #into a separate list
    nums = lotteryNums[count].split()
    while(count2 < len(nums)):
      totalNums.append(int(nums[count2]))       #Converts all strings in a list to int 
      if(count2 < (len(nums) - 1)):
        fiveNums.append(int(nums[count2]))      #Appends it to the five numbers list
      else:
        pBallNums.append(int(nums[count2]))     #Appends it to the Powerball numbers list
      count2 += 1
    count += 1
      
  #Call the function that performs the desired output
  dispFreq(totalNums, fiveNums,pBallNums)
  
  #Close the file
  outfile.close()
  
#_______________________________________________________________  
def dispFreq(TotNums, Fnums, Pnums):
  TotNumsList = list(range(1, 70, 1))   #List of numbers from 1-69 (5 & Powerball numbers)
  FnumsList = list(range(1, 70, 1))     #List of numbers from 1-69 (5 numbers)
  PnumsList = list(range(1, 27, 1))     #List of numbers from 1-26 (Powerball numbers)
  
  #Call function that counts frequency for all in the list
  TotNumsFreq = countFreq(TotNums,TotNumsList)
  TotNumsFreq1 = countFreq(TotNums,TotNumsList) #Made a second copy because didn't know why
  FnumsFreq = countFreq(Fnums,FnumsList)        #when calling NmaxElements, TotNumsFreq was directly
  PnumsFreq = countFreq(Pnums,PnumsList)        #being changed, even though it's not a global variable?
    
  #Call function that finds most common numbers
  topTenNums = NmaxElements(TotNumsFreq,TotNumsList,10)
  print("The 10 most common numbers, ordered by frequency, are:\n",topTenNums,sep="")
  
  #Call function that finds least common numbers
  minTenNums = NminElements(TotNumsFreq1,TotNumsList,10)
  print("\nThe 10 least common numbers, ordered by frequency, are:\n",minTenNums,sep="")

  #Call function that finds the most overdue numbers
  findOverdue(TotNums,TotNumsList)

  #Turn Fnums & Pnums into two different dictionaries, were key = number
  #and the value = its frequency
  FnumsDict = dict(zip(FnumsList,FnumsFreq))
  PnumsDict = dict(zip(PnumsList,PnumsFreq))
  
  print("\nThe frequency of each of the 5 numbers (1-69) between Feb 2010 and May 2016 is:")
  for k in FnumsDict:
    print(k, " =\t", FnumsDict[k],sep="")

  print("\nThe frequency of each Powerball number (1-26) between Feb 2010 and May 2016 is:")
  for k in PnumsDict:
    print(k, " =\t", PnumsDict[k],sep="")
  
#_______________________________________________________________   
#Function that finds N largest elements in a given list
def NmaxElements(numList,rangeList,n):
  topN = []
  
  #Two nested loops that goes through the list n times to find the n largest numbers
  for k in range(0, n):
    maxNum = 0
    count = 0
    
    for j in range(len(numList)):
      if (numList[j] > maxNum):
        maxNum = numList[j] 
        count = j                   #Instead  of saving the frequency of the number,
    numList[count] = 0              #the position is saved instead to later print it
    topN.append(rangeList[count])   #as one of the n common numbers
  
  return topN
  
#_______________________________________________________________
#Function that finds N smalles elements in a given list
def NminElements(numList,rangeList,n):
  lowN = []

  #Two nested loops that goes through the list n times to find the n smallest numbers
  for k in range(0, n):
    minNum = max(numList)
    count = 0
    
    for j in range(len(numList)):
      if (numList[j] < minNum):
        minNum = numList[j] 
        count = j                   #Instead of saving the frequency of the number,
    numList[count] = max(numList)   #the position is saved instead to later print it
    lowN.append(rangeList[count])   #as one of the n common numbers
  
  return lowN

#_______________________________________________________________
#Function that finds the N most overdue numbers in a given list
def findOverdue(numList,rangeList):
  monthNum = [0] * (len(rangeList))
  n = 0     #Counter for the outer while loop
  k = 1     #Counter that keeps track when 6 numbers have passed (change of month)
  month = 1
  
  while(n < len(numList)):
    if (k == 6):                  #Reset for every month  
      month += 1
      k = 0
    monthNum[numList[n] - 1] = month
    k += 1
    n += 1

  #Call the funciton to find the 10 earlieast numbers (numbers closest to Feb, 2010)
  #In other words, numbers with the smallest month count since Feb, 2010
  overdueTenNums = NminElements(monthNum,rangeList,10)
  print("\nThe 10 most overdue numbers, ordered by frequency, are:\n",overdueTenNums,sep="")    
    
#_______________________________________________________________
#Function that finds the frequency of numbers in a list
def countFreq(numList,rangeList):
  freqList = []
  n = 0

  #loop to find the frequency of each number
  while (n < len(rangeList)):
    freq = numList.count(rangeList[n])
    freqList.append(freq)
    n += 1
  
  return freqList


# Call the main function.
main()