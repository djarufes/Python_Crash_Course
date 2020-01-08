########################################################
# Author: David Jarufe                              
# Date: Mar. 2 / 2019
#
# This program determines the type of fluid flow
# through a pipe (Reynolds numbers) using the given
# parameters
########################################################

#Asks user to enter the parameters for the calculation
velocity = float(input("Please enter the water's velocity when flowing through the pipe (m/s or ft/sec) --> "))
diameter = float(input("Please enter the pipe's diameter (m or ft) --> "))
temp = int(input("Pleas enter the water's temperature (C) --> "))

#Determines what Kinematic viscocity to use for calculations
if(temp == 5):         #If temperature is 5 C
    kinemVis = 1.49e-6
elif(temp == 10):      #If temperature is 10 C
    kinemVis = 1.31e-6
elif(temp == 15):      #If temperature is 15 C
    kinemVis = 1.15e-6   

#Calculates the Reynolds number 
reynolds = (velocity * diameter) / kinemVis

#Outputs the final calculation
print("\nReynolds number: ","%.2e" % reynolds, sep="")
