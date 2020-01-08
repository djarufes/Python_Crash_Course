########################################################
# Author: David Jarufe
# Date: Mar. 29 / 2019
# This program prints all the prime numbers
# from 1 to 100
########################################################

#Main Function
def main():
    number = 2   #Counter from 2 - 100
    print("Prime Numbers from 1 - 100")
    print("==========================")
    while(number <= 100):
        is_prime(number)
        number += 1

#Function that finds if a number (testNum) is prime
def is_prime(testNum):
    n = 1                   #Counter from 1 to testNum
    count = 0               #Counter for how many times is testNume divisible with no remainder
    
    while(n <= testNum):    #Loop that checks if testNum is a prime number
        if ((testNum % n) == 0):
            count += 1
        n += 1

    if (count == 2):        #If the number is prime, then it will print
        print(testNum)
        
main()
