########################################################
# Author: David Jarufe
# Date: Mar. 29 / 2019
# This program creates random math questions to be
# answered by the user
########################################################

import random

#Main Function
def main():
    print("\nSolve the following problem:\n")
    quiz_maker()        #Calls the function that generates the quiz

def quiz_maker():
    num_1 = random.randint(100,999)     #Generates the first random number
    num_2 = random.randint(100,999)     #Generates the second random number
    
    print("  ",num_1,sep="")
    print("+ ",num_2,sep="")
    print("-----")

    compAnwer = num_1 + num_2   #Computed summation of both random numbers
    userAnswer = int(input())     #User's answer
    
    if (compAnwer == userAnswer):    #If-else statement that print the final message
        print("\nCorrect!")     #If answer is correct
    else:
        print("\nSorry, the correct answer is --> ", compAnwer,"\n",sep="")    #If answer is incorrect
        
main()
