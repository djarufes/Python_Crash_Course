########################################################
# Author: David Jarufe
# Date: April. 17 / 2019
# This program accepts as input a sentence in which all 
# of the words are run together, but the first character 
# of each word is uppercase. It then converts the 
# sentence to a string in which the words are separated 
# by spaces, and only the first word starts with an 
# uppercase letter.  
########################################################

def main():
    
  #Ask the user for input
  print("\nInput a sentence in which all of the words are run together,",end="")
  print("but the first character of each word is uppercase (remember the period at the end!)",end="")
  sentence = input("-->")
  
  #Call the function that turns the sentence to desied output
  sentConverter(sentence)
  
def sentConverter(sent):
  finalSent = []
  listSent = list(sent)
  count = 0

  #Loop that converts sentence
  while (count < (len(listSent))):
    if (count == 0):                                #Add the first letter
      finalSent.append(listSent[count])
    elif (ord(listSent[count]) < ord('a')):         #If next letter is uppercase
      if (count == (len(listSent) - 1)):            #To prevent printing space before period
        finalSent.append((listSent[count]))
      else:
        finalSent.append(' ')
        finalSent.append((listSent[count]).lower())
    else:                                           #If next letter is lowercase
      finalSent.append(listSent[count])
    count += 1
  
  #Print final converted sentence
  print('')
  print(''.join(finalSent))
  
# Call the main function.
main()
