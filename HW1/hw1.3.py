num=int(input("Enter a number:"))               
temp=num                                         
rev=0
while(num>0):                                 
    dig=num%10                                
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("Your number is palindrome!")
else:
    print("Your is a not palindrome!")

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("Your string is a palindrome")
else:
      print("Your String is not a palindrome")