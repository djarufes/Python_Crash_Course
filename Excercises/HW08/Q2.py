########################################################
# Author: David Jarufe
# Date: April 24 / 2019 & May 3 / 2019
# This program takes a list of gas prices from 1993 -
# 2013 and manipulates it to complete different
# functions
########################################################

import statistics
import matplotlib.pyplot as plt

def main():

  #Open a file for reading
  outfile = open("GasPrices.txt","r")

  #Read the first line from the file
  lineRead = outfile.readline()
  
  #Turns the txt file into a list
  txtData = []
  
  while lineRead !="":
    data = str(lineRead)
    txtData.append(data)

    #Read the next line
    lineRead = outfile.readline()
  
  #Separate all the data in the format MM-DD-YYYY:price to different lists
  month = []
  day = []
  year = []
  gasPrice = []
  tempList = []
  n = 0             #Count for outer loop
  k = 0             #Count for middle loop
  j1= 0             #Counts for inner loops
  j2= 0 
  j3= 0 
  j4= 0 
  count = 0         #Counter that creates the 4 lists
  
  while(n < len(txtData)):
    temp = txtData[n].strip()
    k = 0           #Reset middle counter
    count = 0       #Reset counter that creates the 4 lists
    while(k < len(temp)):
      while(j1 < 2):
        tempList.append(temp[k])
        j1 += 1
        k += 1
      k += 1        #Skip line
      while(j2 < 2):
        tempList.append(temp[k])
        j2 += 1
        k += 1
      k += 1        #Skip line
      while(j3 < 4):
        tempList.append(temp[k])
        j3 += 1
        k += 1
      k += 1        #Skip colon
      
      #Adjust for prices with less than 4 digits (#.### to #.## or #.#)
      if (len(temp) < 15):
        j4 += 2
      elif (len(temp) < 16):
        j4 += 1
        
      while(j4 < 5):
        tempList.append(temp[k])
        j4 += 1
        k += 1
        
      #Creates the different lists
      if(count == 0):
        month.append(int(tempList[0] + tempList[1]))
        day.append(int(tempList[2] + tempList[3]))
        year.append(int(tempList[4] + tempList[5] + tempList[6] + tempList[7]))
        
        #Adjust for prices with less than 4 digits (#.### to #.## or #.#)
        if (len(temp) < 15):
          gasPrice.append(float(tempList[8] + tempList[9] + tempList[10]))
        elif(len(temp) < 16):
          gasPrice.append(float(tempList[8] + tempList[9] + tempList[10] + tempList[11]))
        else:
          gasPrice.append(float(tempList[8] + tempList[9] + tempList[10] + tempList[11] + tempList[12]))
      count = 1
      
    tempList.clear() 
    n += 1              #Increment count for outer loop
    j1 = 0               #Reset counts for inner loops
    j2 = 0 
    j3 = 0 
    j4 = 0 
    
  tempList.clear()
  
  #Call the function that computes the average price per year
  avgPperY(year,gasPrice)
  
  #Call the function that computes the average price per month
  avgPperM(month,gasPrice)
  
  #Call the function that computes the highest and lowest prices per year
  highToLowPperY(day,month,year,gasPrice)
  
  #Call the function that generates a txt file with a list all prices from lowest to highest
  listLowToHigh(day,month,year,gasPrice)
  
  #Call the function that generates a txt file with a list all prices from lowest to highest
  listHighToLow(day,month,year,gasPrice)
  
#Function that finds the average price per year
def avgPperY(year,gasPrice):
  
  #Local variables
  yearMin = min(year)
  yearMax = max(year)
  allYears = []
  meanGas = []
  tempList = []
  
  #Loop that separates data per year
  while(yearMin <= yearMax):
    index1 = year.index(yearMin)        #Index of first gasPrice for that year
    
    if((yearMin - yearMax) == 0):       #Adjust index for last year
      index2 = len(year)
    else:
      index2 = year.index(yearMin + 1)   #Index of last gasPrice for that year
    
    while (index1 < index2):
      tempList.append(gasPrice[index1])
      index1 += 1
    
    allYears.append(yearMin)
    meanGas.append(format(statistics.mean(tempList),".3f"))
    
    #print(yearMin,"\t", format(statistics.mean(tempList),".3f"))
    
    tempList.clear()
    yearMin += 1
  
  tempList.clear()
  #Create the bar graph
  plt.bar(allYears,meanGas)
  
  #Add a title and axis labels
  plt.title("Average Prices Per Year (1993 - 2013)")
  plt.xlabel("Year")
  plt.ylabel("Gas Price ($)")
  
  #Customize the ticks to readjust the previous adjustment
  x_ticks = range(1993,2014,2)
  plt.xticks(x_ticks,x_ticks)
  
  plt.show()

#Function that computes the average price per month
def avgPperM(month,gasPrice):
  #Local variables
  tempMonth= month.copy()
  allMonths = []
  avgGas = []
  tempList = []
  n = 1
  monthIndex = 0
  
  #Loops that gather all the prices per month in a list
  while(n <= 12):
    monthIndex = tempMonth.index(n)
    while (n in tempMonth):
      tempList.append(gasPrice[monthIndex])
      tempMonth[monthIndex] = 0
      if (n in tempMonth):
        monthIndex = tempMonth.index(n)
    allMonths.append(n)
    avgGas.append(float(format(statistics.mean(tempList),".3f")))
       
    tempList.clear()
    n += 1        
  tempList.clear()
  
  #Build the line graph
  plt.plot(allMonths,avgGas, marker="o", label ="line1")
  
  #Add a title and axis labels
  plt.title("Average Prices of Gas Per Month (1993 - 2013)")
  plt.xlabel("Month")
  plt.ylabel("Gas Price ($)")
  
  #Customize the ticks
  x_ticks = range(1,13,1)
  x_months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
  plt.xticks(x_ticks,x_months)
    
  #Add grid & legend
  plt.grid(True)
  plt.legend(["Prices"])
  
  plt.show()
     
#Call the function that computes the highest and lowest prices per year
def highToLowPperY(day,month,year,gasPrice):
  
  #Local variables
  x_months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
  yearMin = min(year)
  yearMax = max(year)
  tempList = []

  print("\nHighest and Lowest Prices Per Year\n")

  #Loop that separates data per year
  while(yearMin <= yearMax):
    index1 = year.index(yearMin)        #Index of first gasPrice for that year
    
    if((yearMin - yearMax) == 0):       #Adjust index for last year
      index2 = len(year)
    else:
      index2 = year.index(yearMin + 1)   #Index of last gasPrice for that year
     
    while (index1 < index2):
      tempList.append(gasPrice[index1])
      index1 += 1  

    minP = min(tempList)
    maxP = max(tempList)
    
    print(yearMin)
    #Prints the lowest price on that year
    print("Lowest\t", x_months[month[tempList.index(minP)] - 1],'. ', end = "", sep = "")
    print(day[tempList.index(minP)], " - ", end = "")
    print(minP)
    
    #Prints the highest price on that year
    print("Highest\t", x_months[month[tempList.index(maxP)] - 1], '. ',end = "", sep = "")
    print(day[tempList.index(maxP)], " - ", end = "")
    print(maxP,"\n")
    
    tempList.clear()
    yearMin += 1
  
  tempList.clear()   
  
def listLowToHigh(day,month,year,gasPrice):
  
  #Local variables
  count = 0
  newGasPrice1 = gasPrice.copy()
  pLen = len(newGasPrice1) 
  
  #Open the file to were the data will be inputed for writing
  outfile = open('GasPricesLowToHigh.txt','w')
  
  #loop that iterates through all prices from least to greatest
  maxP = max(newGasPrice1)
  
  while(count < pLen):
    minP = min(newGasPrice1)
    minInd = newGasPrice1.index(minP)
    monthNum = month[minInd]
    dayNum = day[minInd]
    #Adjust for single digit dates
    if((dayNum < 10) & (monthNum < 10)):
      inputList = ['0',monthNum,'-','0',dayNum,'-',year[minInd],':',minP,'\n']
    elif(dayNum < 10):
      inputList = [monthNum,'-','0',dayNum,'-',year[minInd],':',minP,'\n']
    elif(monthNum < 10):
      inputList = ['0',monthNum,'-',dayNum,'-',year[minInd],':',minP,'\n']
    #Turn the list into a string
    inputString = "".join(map(str, inputList))
    #Write the string into the file
    outfile.write(inputString)
    newGasPrice1[minInd] = maxP + 1
    count += 1
  
  #Close the file
  outfile.close()

def listHighToLow(day,month,year,gasPrice):
    
  #Local variables
  count = 0
  newGasPrice2 = gasPrice.copy()
  pLen = len(newGasPrice2) 
  
  #Open the file to were the data will be inputed for writing
  outfile = open('GasPricesHighToLow.txt','w')
  #loop that iterates through all prices from greatest to least  
  while(count < pLen):
    maxP = max(newGasPrice2)
    maxInd = newGasPrice2.index(maxP)
    monthNum = month[maxInd]
    dayNum = day[maxInd]
    #Adjust for single digit dates
    if((dayNum < 10) & (monthNum < 10)):
      inputList = ['0',monthNum,'-','0',dayNum,'-',year[maxInd],':',maxP,'\n']
    elif(dayNum < 10):
      inputList = [monthNum,'-','0',dayNum,'-',year[maxInd],':',maxP,'\n']
    elif(monthNum < 10):
      inputList = ['0',monthNum,'-',dayNum,'-',year[maxInd],':',maxP,'\n']
    #Turn the list into a string
    inputString = "".join(map(str, inputList))
    #Write the string into the file
    outfile.write(inputString)
    newGasPrice2[maxInd] = 0
    count += 1
  
  #Close the file
  outfile.close()

# Call the main function.
main()
