########################################################
# Author: David Jarufe
# Date: April. 04 / 2019
# This program calculates and displays the total
# rainfall for the year, the average monthly rainfall,
# the months with the highest and lowest amounts. 
########################################################

def main():
  rainFall = []
  count = 0

  #List of month names (just to make the program more fancy)
  monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July',   #Month names
  'August', 'September', 'October', 'November', 'December']

  #Asks user to enter the rainfall per month
  while (count < 12):
    print(monthNames[count])        
    rFall = float(input(" --> "))
    rainFall.append(rFall)          #Adds the input to a list
    count += 1                      #Update while loop variable

  totrFall(rainFall)    #Call to the function that computes everything

#Function that computes all the desired outputs
def totrFall(rainFall):
    rFallSum = 0
    count = 0

    #Sums all the rainfalls
    while (count < 12):
      rFallSum += rainFall[count]
      count += 1

    #Computes the average monthly rainfall
    avgrFall = rFallSum / 12

    print("\nThe total rainfall for the year was ",format(rFallSum,".2f")," in.",sep="")
    print("The average monthly rainfall for the year was ", format(avgrFall,".2f")," in.",sep="")
    print("The highest amount of rainfall for the year was ",max(rainFall)," in.",sep="")
    print("The lowest amount of rainfall for the year was ",min(rainFall)," in.",sep="")

#Call the main function
main()
       
    
