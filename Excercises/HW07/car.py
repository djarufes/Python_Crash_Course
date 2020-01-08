########################################################
# Author: David Jarufe
# Date: April. 19 / 2019
# This program is a Class that can be imported
# for later use
########################################################

#The Car class (car.py)
class Car:
  
  def __init__(self, yearMod, carMake):
    self.__year_model = yearMod
    self.__make = carMake
    self.__speed = 0
    
  #Method that adds 5 from the speed data attribute each time its called
  def accelerate(self):
    self.__speed += 5
  
  #Method that subtracts 5 from the speed data attribute each time its called  
  def brake(self):
    self.__speed -= 5
 
  #This method returns the value of the __speed field
  def get_speed(self):
    return(self.__speed)
  