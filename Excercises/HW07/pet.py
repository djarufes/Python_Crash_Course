########################################################
# Author: David Jarufe
# Date: April. 19 / 2019
# This program is a Class that can be imported
# for later use
########################################################

#The Pet class (pet.py)
class Pet:
  
  def __init__(self, petName, petType, petAge):
    self.__name = petName
    self.__animal_type = petType
    self.__age = petAge
    
  #Method that assigns a value to the __name field
  def set_name(self, nameOfPet):
    self.__name = nameOfPet
  
  #Method that assigns a value to the __animal_type field
  def set_animal_type(self,typeOfPet):
    self.__animal_type = typeOfPet
 
  #Method that assigns a value to the __age field
  def set_age(self,ageOfPet):
    self.__age = ageOfPet
    
  #This method returns the value of the __name field
  def get_name(self):
    return(self.__name)
  
  #This method returns the value of the __animal_type field
  def get_animal_type(self):
    return(self.__animal_type)
  
  #This method returns the value of the __age field
  def get_age(self):
    return(self.__age)
    

     
      
      
      