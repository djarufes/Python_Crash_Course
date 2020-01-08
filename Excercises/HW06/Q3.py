########################################################
# Author: David Jarufe
# Date: April. 11 / 2019
# This program reads a file and then plots its data 
# as a line graph and a bar chart
########################################################

import matplotlib.pyplot as plt

def main():

  #Open a file for reading
  outfile = open("1994_Weekly_Gas_Averages.txt","r")

  #Read the first line from the file
  gas = outfile.readline()
  
  #Turns the txt file into a list
  gasAvg = []
  while gas !="":
    weeklyGas = float(str(gas))
    gasAvg.append(weeklyGas)

    #Read the next line
    gas = outfile.readline()

  #Call function that turns list into a Line Graph
  turnToLineG(gasAvg)
  
  #Call function that turns list into a Bar Graph
  turnToBarG(gasAvg)
  
  #Close the file
  outfile.close()
  
#Function that turns a list to a line graph
def turnToLineG(gasAvg):
  # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.# Create lists with the X,Y coordinates of each data point. # Create lists with the X,Y coordinates of each data point.
  x_coords = []
  count = 0
  while (count < 52):
    x_coords.append(count)
    count += 1
        
  #Build the line graph
  plt.plot(x_coords,gasAvg, marker="o", label ="line1")
  
  #Add a title and axis labels
  plt.title("Weekly Gas Average During 1994")
  plt.xlabel("Week")
  plt.ylabel("Gas Price ($)")
  
  #Customize the ticks
  x_ticks = range(0,53,4)
  y_ticks = [0.992,1.004,1.017,1.029,1.041,1.054,1.066,1.078,1.090,1.103,1.115,1.127,1.140,1.152,1.164,1.177]
  
  plt.xticks(x_ticks,x_ticks)
  plt.yticks(y_ticks,y_ticks)
    
  #Add grid & legend
  plt.grid(True)
  plt.legend(["Prices"])
  
  plt.show()
    
#Function that turns a list to a bar graph
def turnToBarG(gasAvg):
  
  #Variables for the bar graph
  left_edges = [x for x in range(len(gasAvg))]
  heights = []
  count = 0
  #Adjustment so that the bar graph starts at 0
  while (count < 52):
    heights.append(gasAvg[count] - min(gasAvg))
    count += 1

  #Create the bar graph
  plt.bar(left_edges,heights)
  
  #Add a title and axis labels
  plt.title("Weekly Gas Average During 1994")
  plt.xlabel("Week")
  plt.ylabel("Gas Price ($)")
  
  #Customize the ticks to readjust the previous adjustment
  x_ticks = range(0,53,4)
  y_ticks = [0.000,0.015,0.030,0.044,0.059,0.074,0.089,0.103,0.118,0.133,0.148,0.163,0.177,0.192]
  y_ticks_actual = [0.992,1.007,1.022,1.036,1.051,1.066,1.081,1.095,1.110,1.125,1.140,1.155,1.169,1.184]
  
  plt.xticks(x_ticks,x_ticks)
  plt.yticks(y_ticks,y_ticks_actual)

  plt.show()
  
#Call main function
main()
  
  
  
  
  
  
  
  

