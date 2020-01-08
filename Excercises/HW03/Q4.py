########################################################
# Author: David Jarufe
# Date: Mar. 14 / 2019
# This program uses nested loops to draw this pattern:
#
#                   *******
#                   ******
#                   *****
#                   ****
#                   ***
#                   **
#                   *
########################################################

#Asks user for number of layers
layers = int(input("How many layers would you like the right triangle to have? --> "))

layersDup1 = layers  #Just another variable with the value of layers
print()

#Nested loops to create pattern
while(layersDup1 > 0):
    layersDup2 = layersDup1
    layersDup1 -= 1
    while(layersDup2 > 0):
        print("*",end="")
        layersDup2 -= 1
    print()
print()
        
