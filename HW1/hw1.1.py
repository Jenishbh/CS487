def numbers_to_strings(argument):      
    myDict = {}
    for key in ['A', 'B', 'C']:  #Multiple key has one value
      myDict[key] = 2             #value assign 
    for key in['G','H','I']:
      myDict[key] = 4
    for key in['M','N','O']:
      myDict[key] = 6
    for key in['T','U','V']:
      myDict[key] = 8
    for key in['D','E','F']:
      myDict[key] = 3
    for key in['J','K','L']:
      myDict[key] = 5
    for key in['P','S','R']:
      myDict[key] = 7
    for key in['W','X','Y']:
      myDict[key] = 9
    if myDict.get(argument):                                                                                            #If user input on of the key then print the succuess message
      print("The digit", myDict.get(argument),"corresponds to the letter", argument, "on the telephone.")
    else:
      print("There is no digit on the telephone that corresponds to",argument)                                          #else print false message

    
    return ""
     
  
#main function

argument=input("Enter a single letter, and I will tell you what the corresponding digit is on the telephone.")
if argument.isupper()==True:                                                                                          #fillter user input
  print (numbers_to_strings(argument)) 
else:
  print("Invalid Entry")