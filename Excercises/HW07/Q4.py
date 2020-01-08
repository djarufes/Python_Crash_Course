########################################################
# Author: David Jarufe
# Date: April. 19 / 2019
# This program creates an object of a class and 
# prompts the user to input data that willl later be
# displayed on the screen
########################################################

import pet

def main():

    #Ask user for pet's attributes
    pName = input("What is your pet's name?\t--> ")
    pType = input("What type of pet is this?\t--> ")
    pAge = input("What is your pet's age?\t\t--> ")
    
    #Create a Pet object
    petClass = pet.Pet(pName,pType,pAge)  
    
    #Saves the inputs
    petClass.set_name(pName)
    petClass.set_animal_type(pType)
    petClass.set_age(pAge)
    
    #Outputs pet's attributes
    print("\nYour pet's name is:\t", petClass.get_name(), sep="")
    print("Your pet is a:\t\t", petClass.get_animal_type(), sep="")
    print("Your pet's age is:\t", petClass.get_age(), sep="")
    
# Call the main function.
main()



