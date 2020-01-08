########################################################
# Author: David Jarufe
# Date: April. 11 / 2019
# This program created a dictionary containing the
# U.S. states as keys and their capitals as values.
# It also quizes the user by asking them random states.
# so that the user enters the capital.
########################################################
import random

#The main function
def main():
    
  #List of all the states and their capitals of U.S.
  states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
            "Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
            "Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri",
            "Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
            "North Carolina","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
            "North Dakota","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington",
            "West Virginia","Wisconsin","Wyoming"]
  capitals = ["Montgomery","Juneau","Phoenix","Little Rock","Sacramento","Denver","Hartford","Dover",
            "Tallahassee","Atlanta","Honolulu","Boise","Springfield","Indianapolis","Des Moines","Topeka",
            "Frankfort","Baton Rouge","Augusta","Annapolis","Boston","Lansing","Saint Paul","Jackson",
            "Jefferson City","Helena","Lincoln","Carson City","Concord","Trenton","Santa Fe","Albany",
            "Raleigh","Columbus","Oklahoma City","Salem","Harrisburg","Providence","Columbia","Bismarck",
            "Pierre","Nashville","Austin","Salt Lake City","Montpelier","Richmond","Olympia","Charleston",
            "Madison","Cheyenne"]
  
  #Turn the two lists (states,capitals) into a dictionary (key,values)
  stateCapDic = dict(zip(states,capitals))
  
  #Call the function that generates the random decisions as a list
  rands = randNum(50)

  #Call the function that generates the quiz for the user to answer
  stateCapQuiz(stateCapDic,states,rands)
  
#Function that creates a list of randomly generated numbers
def randNum(nums):
  
  #Create a list of randomly generated numbers in the range of "nums"
  randList = random.sample(range(nums), nums)
  
  #Return the generated list to main
  return randList

#Funciton that randomly quizes the user
def stateCapQuiz(stateCapDic,states,rands):
    
  print("Welcome to the U.S. States and Capitals quiz!")
  print("Let the quiz BEGIN!")
  
  #Begin questioning the user
  count = 0
  correct = 0
  wrong = 0
  
  #Keeps questioning until the user wants to stop or until it reaches 50 questions
  while(count < 50):
    chosenState = states[rands[count]]
    print("\nWhat is the capital of ",chosenState,"?",end="",sep="")
    answer = input("--> ")
    
    #If answer is correct
    if(answer == stateCapDic.get(chosenState)):
      print("\nThat's correct!")
      correct += 1
      
      print("Correct \t",correct,sep="")
      print("Wrong \t\t",wrong,sep="")
      
      print("\nPress enter to continue or type 'Done' to finish the quiz",end="")
      nextQuestion = input()
      
      #Print final scores if the user want to finish
      if((nextQuestion == "Done") | (nextQuestion == "done")):
        print("Final Scores are:")
        print("Correct \t\t",correct,sep="")
        print("Wrong \t\t",wrong,sep="")
        count = 51
          
      else:
        count += 1
    
    #If answer is incorrect
    else:
      print("\nThat's incorrect! The correct answer is ",stateCapDic.get(chosenState), sep="")
      wrong += 1
      
      print("Correct \t",correct,sep="")
      print("Wrong \t\t",wrong,sep="")
      
      print("\nPress enter to continue or type 'Done' to finish the quiz",end="")
      nextQuestion = input()
      
      #Print final scores if the user want to finish
      if((nextQuestion == "Done") | (nextQuestion == "done")):
        print("\nFinal Scores are:")
        print("Correct \t",correct,sep="")
        print("Wrong \t\t",wrong,sep="")
        count = 51
          
      else:
        count += 1    
        
  #Print final scores if the user continuously answers the 50 questions
  if(count == 50):
    print("\nFinal Scores are:")
    print("Correct \t",correct,sep="")
    print("Wrong \t\t",wrong,sep="")
  
#Call main function
main()
  

