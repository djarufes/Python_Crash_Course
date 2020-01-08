########################################################
# Author: David Jarufe
# Date: April. 04 / 2019
# This program reads the number of steps you took from
# a file and outputs the average for each month
########################################################

#Declarations of constants
JAN = 31
FEB = 28
MAR = 31
APR = 30
MAY = 31
JUNE = 30
JULY = 31
AUG = 31
SEPT = 30
OCT = 31
NOV = 30
DEC = 31

def main():

  #Open a file for writing
  outfile = open("steps.txt","r")

  #List of month names (just to make the program more fancy)
  monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July',   #Month names
  'August', 'September', 'October', 'November', 'December']

  #Turns the txt file into a list
  steps = [outfile.readline().strip() for _ in range(365)]
  count = 0
  
  #while (count < 365):
  #  print(steps[count])
  #  count += 1
  
  #Calls the function that computes the step average per month
  stepAvg(steps[0:31],JAN,monthNames[0])
  stepAvg(steps[31:59],FEB,monthNames[1])
  stepAvg(steps[59:90],MAR,monthNames[2])
  stepAvg(steps[90:120],APR,monthNames[3])
  stepAvg(steps[120:151],MAY,monthNames[4])
  stepAvg(steps[151:181],JUNE,monthNames[5])
  stepAvg(steps[181:212],JULY,monthNames[6])
  stepAvg(steps[212:243],AUG,monthNames[7])
  stepAvg(steps[243:273],SEPT,monthNames[8])
  stepAvg(steps[273:304],OCT,monthNames[9])
  stepAvg(steps[304:334],NOV,monthNames[10])
  stepAvg(steps[334:365],DEC,monthNames[11])

 #Close the file
  outfile.close()

def stepAvg(steps,month,mName):

  #Variable initialization
  count = 0
  stepSum = 0

  #While loop that sum all the steps for the month
  while (count < month):
    stepSum = stepSum + int(str(steps[count]))
    count += 1

  #Computes the step average and print the final output
  avg = stepSum / month
  print(mName," -> ",format(avg,".0f")," steps!",sep="")

#Call the main function
main()
