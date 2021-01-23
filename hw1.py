import random
import math



    
def successful():#class for successful message 
  print("Congratulations you did it in ", count, " try")

def Sorry():# class for showing message after 5 times user failed 
  print("sorry ")

lower=int(input("Enter starting number: ")) # Get first number
upper=int(input("Enter your ending number: "))# get last number

x=random.randint(lower,upper)#genrate random number
#print(x) # #chk the function



count = 0# counter for give user 5 chance

while count < 5:
  count +=1 # count incress
  guss=int(input("Guess a number"))# get a guess from user
  if x == guss: # if is't same 
    successful() # call the class
    break; # because user get it then force stop the function 
  elif x > guss:# if the guess is smaller then the number
    if x - guss == 1: # if the guess is small but near the number
      print("Your Anshwer is closs but you need to guss one more time")
    else:
      print("You guessed too small!")
  elif x < guss:# if the guess is bigger
    if guss - x == 1:# if the guess is biger but near the number
      print("Your Anshwer is closs but you need to guss one more time")
    else:
      print("You guessed too high!")

if count >= 5: # after 5 turns
   print("\nThe number is %d"%x)
   print("\tBetter Luck Next time!")
