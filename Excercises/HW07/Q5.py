########################################################
# Author: David Jarufe
# Date: April. 19 / 2019
# This program creates an object of a class that accepts 
# a cars year model and make and later accelerates or 
# decelerates the speed of a car.
########################################################

import car

def main():
    
  #Ask user for car's attributes
  cYModel = input("What is your car's year model?\t--> ")
  cMake = input("What is the make of your car?\t--> ")
  
  #Create a Car object
  carClass = car.Car(cYModel,cMake) 
    
  #Accelerate car 5 times
  n = 0
  print("\nCar's Current Speed (mi/h):\n")
    
  while (n < 5):
    carClass.accelerate()
    print(carClass.get_speed())
    n += 1
      
  #Decelerate car 5 times
  n = 0
  while (n < 5):
    carClass.brake()
    print(carClass.get_speed())
    n += 1

# Call the main function.
main()