########################################################
# Author: David Jarufe
# Date: April. 20 / 2019
# This program creates finds the area under the curve
# by using the trapezoid rule
########################################################
import math

#Constants
TRAP = 1000

def main():
  
  #Ask the user for the inputs
  print("Welcome to the Numerical Integration Calculator")
  
  boundA = int(input("Choose a lower bound > 0 --> "))
  
  #Check for invalid lower bound
  j = 0
  fail = 0
  if (boundA <= 0):
    while (j < 3):
      if ((boundA <= 0) &  (j < 2)):
        boundA = int(input("Sorry, please choose a lower bound > 0 --> "))
      elif ((boundA <= 0) &  (j == 2)):  
        boundA = print("\nTo many incorrect attempts!")
        fail = 1
      elif(boundA <= 0):
        fail = 0
        break
      j += 1
  else:
    fail = 0
      
  #Check for invalid upper bound
  j = 0
  if (fail == 0):
    boundB = int(input("Choose an upper bound > lower bound --> "))
    
    if (boundB <= boundA):
      while (j < 3):
        if ((boundB <= boundA) &  (j < 2)):
          boundB = int(input("Sorry, please choose an upper bound > lower bound --> "))
        elif ((boundB <= boundA) & (j == 2)):  
          boundB = print("\nTo many incorrect attempts!")
          fail = 1
        elif(boundB > boundA):
          fail = 0
          break
        j += 1
    else:
      fail = 0
    
    if (fail == 0):
      print("\nIntegration of sqrt(x)")
      print("Lower band of", format(boundA,".4f")) 
      print("Upper bound of", format(boundB,".4f"))

      #Calls function that computes the integration
      trapInteg(func, boundA, boundB, TRAP)
  
#The function that will be computed 
def func(x):
  return math.sqrt(x)
  
#Function that computes the integration
def trapInteg(inF, bA, bB, n):
  funcH = (bB - bA) / n                 #Function step size
  funcS = (0.5) * (inF(bA) + inF(bB))   #Sum of all computations
  
  for k in range (1, n, 1):
    funcS =  funcS + inF(bA + (k * funcH))

  finAns = funcH * funcS
  print("\nFinal answer = ",format(finAns,".4f")) 

# Call the main function.
main()