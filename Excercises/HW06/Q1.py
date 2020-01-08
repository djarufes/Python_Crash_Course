########################################################
# Author: David Jarufe
# Date: April. 10 / 2019
# This program accepts the user input for the sales of
# each month and plots them into a pie chart.
########################################################

import matplotlib.pyplot as plt

def main():
  #Variable declarations
  sales = []
  count = 0
    
  #List of month names (just to make the program more fancy)
  monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July',   #Month names
  'August', 'September', 'October', 'November', 'December']
  
  #Asks user to eneter the sales for each month
  while (count < 12):
    print(monthNames[count],sep="")        
    monthlySale = float(input(" --> "))
    sales.append(monthlySale)          #Adds the input to a list
    count += 1  
    
  plotIt(sales,monthNames) #Call to the function that plots everything
    
def plotIt(sales,monthNames):
  
  #Color tuple used for the chart
  sliceColor = ['r', 'g', 'b', 'y', 'm', 'w', 'k', 'blue', 'pink', 'brown', 'ivory', 'black']
  
  #Create a pie chart from the values
  plt.pie(sales,labels=monthNames,colors=sliceColor)
  
  # Add a title.
  plt.title('Sales by Month')
  
  # Display the pie chart.
  plt.show()

# Call the main function.
main()
