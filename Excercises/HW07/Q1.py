########################################################
# Author: David Jarufe
# Date: April. 17 / 2019
# This program calculates the average number of words 
# per sentence from a paragraph in a .txt file
########################################################

def main():

  #Open a file for reading
  outfile = open("text.txt","r")

  #Read the first line from the file
  lineRead = outfile.readline()
  
  #Turns the txt file into a list
  paragraph = []
  while lineRead !="":
    sentence = str(lineRead)
    paragraph.append(sentence)

    #Read the next line
    lineRead = outfile.readline()
  
  #Call function that calculates the average number of words per sentence.
  avgWperS(paragraph)
    
  #Close the file
  outfile.close()

def avgWperS(par):
  
  #Variable declarations
  count = 0
  words = 0
  avgWords = 0
  
  #Find average number of words per sentence
  while(count < len(par)):
    sent = par[count].strip()
    
    #Split the sentence into words
    words += len(sent.split())
    count += 1
    
  #Calculate average
  avgWords = words / len(par)
  
  #Prints the final output
  print("\nThe average number of words per sentence in this paragraph is ", int(avgWords), "!", sep="")

# Call the main function.
main()













