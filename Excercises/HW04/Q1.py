########################################################
# Author: David Jarufe
# Date: Mar. 29 / 2019
# This program calculates the distance an object has
# fallen during a time interval given a falling time
########################################################

#Declarations of constants
GRAVITY = 9.8 #Speed of gravity (m/s)

#Main function
def main():
    f_time = 1                      #Falling time (in seconds)
    print("\nApproximate Falling Distance per Second")
    print("=======================================")
    print("TIME (s)\t|\t DISTANCE (m)\n")
    
    while (f_time <= 10):
        falling_distance(f_time)    #The function is called with given inputs
        f_time += 1 

#Function that calculates the falling distance given the time as input 
def falling_distance(f_time):
    dist = (1/2) * GRAVITY * (f_time ** 2)      #Calulates the final distance
    print(f_time,"\t\t|\t ",format(dist,".2f"),sep="")

main()  #Calling main for final result
    

    
