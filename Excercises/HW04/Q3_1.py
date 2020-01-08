########################################################
# Author: David Jarufe
# Date: Mar. 29 / 2019
# This program finds if a number is a prime number
########################################################

#Main Function
def main():
    number = int(input("\nPlease input the you want to test --> "))
    is_prime(number)

#Function that finds if a number (testNum) is prime
def is_prime(testNum):
    n = 1   #Counter from 1 to testNum
    count = 0   #Counter for how many times is testNume divisible with no remainder
    
    while(n <= testNum):     #Loop that checks if testNum is a prime number
        if ((testNum % n) == 0):
            count += 1
        n += 1

    if (count == 2):
        print(testNum," is a prime number!\n",sep="")
    else:
        print(testNum," is not a prime number!\n",sep="")
        
main()
    
    
